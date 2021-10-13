
def search_polynomials(n: int):
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

    pivots = generate_pivots(n)
    del(pivots[-1])
    # print(pivots)

    seed = [0 for _ in range(n)]
    seed[-1] = 1

    polynomials = list()

    for polynomial in pivots:
        nums = simulate(n, seed, polynomial)
        if len(nums) == 2**n - 1:
            polynomials.append(polynomial)

    # print(polynomials)
    return polynomials


def simulate(n: int, seed: list, polynomial: list, scrambling: list = None) -> list:
    """
        scrambling[i] = j means the i-th bit in output is connected to the j-th bit before
    :param n: 
    :param seed: 
    :param polynomial: 
    :param scrambling: 
    :return: 
    """
    def get_num(binary: list, scrambling: list = None) -> int:
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

    def process(n: int, cur: list, poly: list) -> list:
        node = cur[-1]
        for p in poly:
            # if p != 0 and p != n - 1:
            node ^= cur[p]

        cur.insert(0, node)
        del(cur[-1])
        return cur

    output = list()
    numbers = set()
    cur = seed.copy()

    # num = get_num(cur)
    # output.append(num)
    # numbers.add(num)

    while True:
        num = get_num(cur, scrambling)
        if num in numbers:
            break
        numbers.add(num)
        output.append(num)
        cur = process(n, cur, polynomial)

    return output


if __name__ == '__main__':
    # print(LFSR.simulate(4, [0,0,0,1], [0,1]))

    # print(LFSR.search_polynomials(5))

    N = 5



    import Utils
    scramblings = Utils.generate_scrambling(N)

    seed = [0 for _ in range(N)]
    seed[-1] = 1

    polynomials = search_polynomials(N)
    # for poly in polynomials:
    #     print(LFSR.simulate(N, seed, poly))
    for scram in scramblings:
        print(simulate(N, seed, polynomials[0], scram))
