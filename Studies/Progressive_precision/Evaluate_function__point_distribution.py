import math

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

def evaluate_2(n: int, nums: list) -> int:
    ans = 0
    # print(nums)
    for i in range(max(1, n - 3), n):
        count = [0 for _ in range(2**i)]
        zeros = 2**i
        for j in range(2**i):
            # TODO: think twice here
            if j == 2**n - 1:
                break

            index = math.ceil(nums[j] / 2**n * 2**i) - 1
            if count[index] == 0:
                zeros -= 1
            count[index] += 1

            assert zeros == sum([1 if a == 0 else 0 for a in count])
        ans += zeros

        for k in range(2**n - 1):
            index_1 = math.ceil(nums[k] / 2**n * 2**i) - 1
            index_2 = math.ceil(nums[k + 2**i] / 2**n * 2**i) - 1
            if count[index_1] == 1:
                count[index_1] = 0
                zeros += 1
            elif count[index_1] > 1:
                count[index_1] -= 1

            if count[index_2] == 0:
                zeros -= 1
            count[index_2] += 1

            assert zeros == sum([1 if a == 0 else 0 for a in count])
        ans += zeros

    return ans



if __name__ == '__main__':

    N = 6
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

                value = evaluate_2(N, num_sequence_rotate)

                # if not priority_queue.empty() and value > priority_queue.last_value():
                #     continue

                set_t = Setting(poly, seed, scram, value)

                priority_queue.add(set_t)
                if priority_queue.length() > 200:
                    priority_queue.sort()
                    priority_queue.remove_half()

    priority_queue.sort()
    priority_queue.print()
