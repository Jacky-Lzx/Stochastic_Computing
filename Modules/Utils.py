
def generate_scrambling(n: int) -> list:
    from itertools import permutations
    ans = list(permutations(range(n)))
    # print(ans)
    return ans


def nums_to_bit_arrays(n: int, nums: list) -> list:
    ans = list()
    for num in nums:
        ans.append(num_to_arr(n, num))
    return ans


def bit_arrays_to_nums(n: int, bit_arrays: list) -> list:
    ans = list()
    length = n
    for bit_array in bit_arrays:
        multiplier = 1
        result = 0
        for i in range(length - 1, -1, -1):
            result += multiplier * bit_array[i]
            multiplier *= 2
        ans.append(result)
    return ans


def num_to_arr(n: int, num: int) -> list:
    ans = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        ans[i] = num % 2
        num //= 2
    return ans


def comparator(arr: list, num: int, le=False):
    ret = arr.copy()
    for i, r in enumerate(ret):
        if le and r == num:
            ret[i] = 1
        elif r < num:
            ret[i] = 1
        else:
            ret[i] = 0
    return ret


def count_arr(arr: list):
    num = 0
    for a in arr:
        if a == 1:
            num += 1
    return num


def DFF(arr: list, num: int) -> list:
    first = arr[0: num]
    second = arr[num:]
    second.extend(first)
    return second


if __name__ == '__main__':
    # generate_scrambling(5)
    # bit_arrays = nums_to_bit_arrays(5, [2, 5, 3, 4, 6, 7])
    # print(bit_arrays)
    # nums = bit_arrays_to_nums(5, bit_arrays)
    # print(nums)
    arr = [i for i in range(10)]
    # ret = comparator(arr, 5, False)
    # print(arr)
    # print(ret)
    #
    # ret = comparator(arr, 5, True)
    # print(arr)
    # print(ret)
    ret = DFF(arr, 2)
    print(ret)
    print(arr)
    ret[2] = 0
    print(arr)
    # print(num_to_arr(5, 30))

