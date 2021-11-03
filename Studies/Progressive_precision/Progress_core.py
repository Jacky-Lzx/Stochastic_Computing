from typing import List
from Modules import Utils


def simulate(n: int, nums_1: list, nums_2: list, circuit_fn, real_fn, le: bool = False):
    LEN = 2**n
    MAEs = [0 for _ in range(2 * n + 1)]
    x_arr = range(LEN)
    y_sim = [[0 for _ in range(LEN)] for __ in range(2 * n + 1)]
    for j in range(max(1, n - 3), 2 * n + 1):
        for x in range(LEN):
            bitstream_1 = Utils.comparator(nums_1, x, le)
            bitstream_2 = Utils.comparator(nums_2, x, le)
            output = circuit_fn(bitstream_1, bitstream_2)

            y_sim[j][x] = Utils.count_arr(output[:2**j]) / (2**j)
            MAEs[j] += abs(y_sim[j][x] - real_fn(x))

    for j in range(max(1, n - 3), 2 * n + 1):
        MAEs[j] /= LEN

    print(y_sim)
    print(MAEs)

    # from matplotlib import pyplot as plt
    # y_real = [real_fn(x) for x in x_arr]
    # plt.plot(x_arr, y_real)
    # # for j in range(n - 3, 2 * n + 1):
    # #     plt.plot(x_arr, y_sim[j])
    # for j in range(2 * n - 2, 2 * n + 1):
    #     plt.plot(x_arr, y_sim[j])
    # plt.show()

    return MAEs


def rotate(nums_1: list, nums_2: list) -> tuple:
    new_1 = list()
    new_2 = list()

    length = len(nums_2)
    if nums_1 is not None:
        assert length == len(nums_1)

    if nums_1 is not None:
        for i in range(length):
            new_1.extend(nums_1)

    temp = nums_2
    for i in range(length):
        new_2.extend(temp)
        temp = Utils.DFF(temp, 1)

    # print(nums_1)
    # print(new_1)
    # print(nums_2)
    # print(new_2)

    return new_1, new_2


if __name__ == '__main__':
    N = 1
    num_1 = [0, 1]
    num_2 = [0, 1]
    new_1, new_2 = rotate(num_1, num_2)
    print(new_1)
    print(new_2)

    LEN = 2**N

    def and_fn(x, y): return [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    def real_fn(x): return x**2 / LEN**2

    simulate(N, new_1, new_2, and_fn, real_fn, le=False)

