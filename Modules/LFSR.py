from typing import Tuple, List


class LFSR:
    class setting:
        def __init__(self, seed: List[int], polynomial: List[int], scrambling: List[int] = None, inverter: List[int] = None, inserting_zero: bool = False, zero_position: int = -1):
            """
            :param seed:
            :param polynomial:
            :param scrambling: scrambling[i] = j means the i-th bit in output is connected to the j-th bit before
            :param inverter:
            :param inserting_zero:
            :param zero_position:
            """
            self.seed = seed
            self.polynomial = polynomial
            self.scrambling = scrambling
            self.inverter = inverter
            self.inserting_zero = inserting_zero
            self.zero_position = zero_position

    def __init__(self, N: int, LFSR_inverter: List[int] = None):
        self.N = N
        if LFSR_inverter is not None:
            assert N == len(LFSR_inverter)
        self.LFSR_inverter = LFSR_inverter

    # TODO: inverting
    def simulate(self, a_setting: setting):
        def get_num(binary: List[int], scrambling: List[int] = None) -> int:
            length = len(binary)
            multiplier = 1
            result = 0
            if scrambling is None:
                for i in range(length - 1, -1, -1):
                    result += multiplier * binary[i]
                    multiplier *= 2
            else:
                for i in range(length - 1, -1, -1):
                    result += multiplier * binary[scrambling[i]]
                    multiplier *= 2
            return result

        def process(n: int, cur: List[int], poly: List[int], inverter: List[int]) -> List[int]:
            node = cur[-1]
            for p in poly:
                # if p != 0 and p != n - 1:
                node ^= cur[p]

            cur.insert(0, node)
            del (cur[-1])

            if inverter is not None:
                for i, num in enumerate(inverter):
                    if num == 1:
                        if i == n - 1:
                            continue
                        cur[i + 1] ^= 1
            return cur

        output = list()
        numbers = set()
        cur = a_setting.seed.copy()

        index = 0
        while True:
            num = get_num(cur, a_setting.scrambling)
            if num in numbers:
                break
            # print(cur)
            numbers.add(num)
            output.append(num)
            cur = process(self.N, cur, a_setting.polynomial, self.LFSR_inverter)

            index += 1

        # Inserting missing number
        if a_setting.inserting_zero:
            for i in range(2**self.N):
                if i not in numbers:
                    output.insert(a_setting.zero_position, i)
        return output

    def search_polynomials(self):
        def generate_pivots(n: int):
            def helper(n: int, index: int, cur_list: list, ans: list):
                if index == n - 1:
                    ans.append(cur_list.copy())
                    return
                cur_list.append(index)
                helper(n, index + 1, cur_list, ans)
                del(cur_list[-1])
                helper(n, index + 1, cur_list, ans)

            ans = list()
            helper(n, 0, list(), ans)
            return ans

        pivots = generate_pivots(self.N)
        del(pivots[-1])

        seed = [0 for _ in range(self.N)]
        seed[-1] = 1

        polynomials = list()
        for polynomial in pivots:
            a_setting = LFSR.setting(seed, polynomial)
            nums = self.simulate(a_setting)
            if len(nums) == 2**self.N - 1:
                polynomials.append(polynomial)
        return polynomials

    def set_inverter(self, inverter: List[int]) -> None:
        self.LFSR_inverter = inverter


if __name__ == '__main__':
    import Utils
    N = 8
    polys_record = None
    inverters = Utils.generate_seeding(N)
    for inverter in inverters:
        print(f"LFSR_inverter: {inverter}")

        lfsr = LFSR(N, inverter)
        polys = lfsr.search_polynomials()
        if polys_record is None:
            polys_record = polys.copy()
        else:
            assert polys_record == polys
        print(polys)
        seed = [0 for _ in range(N)]
        seed[-1] = 1

        a_setting = LFSR.setting(seed, polys[0], None, None, True, 0)
        bitstream = lfsr.simulate(a_setting)
        # print(bitstream)

    # print(len(polys))
