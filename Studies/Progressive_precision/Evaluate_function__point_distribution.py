import math

from typing import List, Tuple

from Modules import LFSR, Utils


class Setting:
    def __init__(self, poly, seed, scram, value):
        self.poly = poly
        self.seed = seed
        self.scram = scram
        self.value = value

    def val(self):
        return self.value

    def __str__(self):
        return "poly: {}\nseed: {}\nscram: {}\nvalue: {}\n".format(self.poly, self.seed, self.scram, self.value)


def evaluate(n: int, nums: list) -> int:
    # TODO: temp here: we only have 2^n -1 numbers in total, it is a little different than sobol sequence
    ans = 0
    for i in range(max(1, n - 3), n + 1):
        count = [0 for _ in range(2**i)]
        for j in range(2**i):
            # TODO: think twice here
            if j == 2**n - 1:
                break
            count[math.ceil(nums[j] / 2**n * 2**i) - 1] = 1
        # print(count)
        ans += 2**i - sum(count)
        # print(ans)
    return ans


def distance(n: int, nums: List[int]) -> Tuple[int, List[int]]:
    length = len(nums)
    LEN = 2**n
    count = [0 for _ in range(length)]
    zeros = length
    for i, num in enumerate(nums):
        # index = math.floor(nums[i] * length / LEN)
        index = math.ceil(nums[i] * length / LEN) - 1
        if count[index] == 0:
            zeros -= 1
        count[index] += 1

        # assert zeros == sum([1 if a == 0 else 0 for a in count])
    return zeros, count


def evaluate_2(n: int, nums: list) -> int:
    ans = 0
    for i in range(max(1, n - 3), n):
        zeros, _ = distance(n, nums[:2**i])
        ans += zeros

    # print(f"Before :{ans}")
    # length = len(nums)
    for j in range(2**n):
        for i in range(n + 1, 2*n):
            zeros, _ = distance(n, nums[j:j + 2**(i - n)])
            ans += zeros

    # print(f"After: {ans}")
    return ans


def evaluate_3(n: int, nums: list) -> int:
    ans = 0
    for i in range(max(1, n - 3), n):
        zeros, _ = distance(n, nums[:2**i])
        ans += zeros

    # print(f"Before :{ans}")
    # length = len(nums)
    ans_2 = 0
    for j in range(2**n):
        for i in range(n + 1, 2*n):
            zeros, _ = distance(n, nums[j:j + 2**(i - n)])
            ans_2 += zeros

    ans += ans_2 / (2**n - 1)
    # print(f"After: {ans}")
    return ans


if __name__ == '__main__':
    N = 5
    LEN = 2**N
    print(f"N = {N}")
    polynomials = LFSR.search_polynomials(N)
    print(f"polynomials = {polynomials}")
    seeds = Utils.generate_seeding(N)
    print(f"seeds = {seeds}")
    scramblings = Utils.generate_scrambling(N)
    print(f"scramblings = {scramblings}")

    # print(evaluate(3, [1, 4, 6, 7, 3, 5, 2]))
    # from queue import PriorityQueue
    from Modules.Data_structure import Priority_queue

    priority_queue = Priority_queue()

    import Progress_core

    for poly in polynomials:
        print("Now: {}".format(poly))
        for seed in seeds:
            for scram in scramblings:
                num_sequence = LFSR.simulate(N, seed, poly, scram)

                _, num_sequence_rotate = Progress_core.rotate(N, None, num_sequence)

                value = evaluate_3(N, num_sequence_rotate)

                # if not priority_queue.empty() and value > priority_queue.last_value():
                #     continue

                set_t = Setting(poly, seed, scram, value)

                priority_queue.add(set_t)
                if priority_queue.length() > 1000:
                    priority_queue.sort()
                    priority_queue.remove_half()

    priority_queue.sort()
    while priority_queue.length() > 100:
        priority_queue.remove_half()
    priority_queue.print()
