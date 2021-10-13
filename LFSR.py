class LFSR:
    @staticmethod
    def search_polynomial(n: int):
        def generate_pivots(n: int):
            def helper(n: int, index: int, cur_list: list, ans: list):
                if index == n:
                    ans.append(cur_list.copy())
                    return

                cur_list.append(index)
                helper(n, index + 1, cur_list, ans)
                del(cur_list[-1])
                helper(n, index + 1, cur_list, ans)

            ans = list()
            helper(n, 0, list(), ans)
            return ans

        ans = generate_pivots(n)
        print(ans)
         # TODO: finish it

    @staticmethod
    def simulate(n: int, seed: list, polynomial: list):
        def get_num(binary: list) -> int:
            length = len(binary)
            multiplier = 1
            result = 0
            for i in range(length - 1, -1, -1):
                result += multiplier * binary[i]
                multiplier *= 2
            return result

        def process(cur: list, poly: list) -> list:
            node = cur[-1]
            for p in poly:
                node ^= cur[p]

            cur.insert(0, node)
            del(cur[-1])
            return cur

        output = list()
        cur = seed
        output.append(get_num(seed))
        while True:
            cur = process(cur, polynomial)
            num = get_num(cur)
            if num == output[0]:
                break
            output.append(num)

        return output


if __name__ == '__main__':
    print(LFSR.simulate(4, [0,0,0,1], [0,1]))

    # LFSR.search_polynomial(4)
