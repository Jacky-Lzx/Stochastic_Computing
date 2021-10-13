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

    # priority_queue = PriorityQueue()

    for poly in polynomials:
        print("Now: {}".format(poly))
        for seed in seeds:
            for scram in scramblings:
                num_sequence = LFSR.simulate(N, seed, poly, scram)

                value = evaluate(N, num_sequence)

                set = Setting(poly, seed, scram, value)

                priority_queue.add(set)
                if priority_queue.length() > 100:
                    priority_queue.remove_last()


    priority_queue.print()
