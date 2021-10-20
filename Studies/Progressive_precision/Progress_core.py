from Modules import Utils


def simulate(n: int, nums_1: list, nums_2: list, circuit_fn, real_fn):
    LEN = 2**n
    MAEs = [0 for _ in range(2 * n + 1)]
    x_arr = range(LEN)
    y_sim = [[0 for _ in range(LEN)] for __ in range(2 * n + 1)]
    y_real = [real_fn(x) for x in x_arr]
    for j in range(n - 3, 2 * n + 1):
        for x in range(LEN):
            bitstream_1 = Utils.comparator(nums_1, x, le=True)
            bitstream_2 = Utils.comparator(nums_2, x, le=True)

            output = circuit_fn(bitstream_1, bitstream_2)

            if j == 2 * n:
                # TODO: inserting zeros changes this result.
                y_sim[j][x] = Utils.count_arr(output[:(2**n - 1)**2]) / (2**n - 1)**2
            else:
                y_sim[j][x] = Utils.count_arr(output[:2**j]) / (2**j)

            MAEs[j] += abs(y_sim[j][x] - real_fn(x))

    for j in range(n - 3, 2 * n + 1):
        MAEs[j] /= LEN

    print(y_sim)
    print(MAEs)

    # from matplotlib import pyplot as plt
    # plt.plot(x_arr, y_real)
    # # for j in range(n - 3, 2 * n + 1):
    # #     plt.plot(x_arr, y_sim[j])
    # for j in range(2 * n - 2, 2 * n + 1):
    #     plt.plot(x_arr, y_sim[j])
    # plt.show()

    return MAEs


def rotate(n: int, nums_1: list, nums_2: list) -> tuple:
    new_1 = list()
    new_2 = list()
    if nums_1 is not None:
        for i in range(2**n - 1):
            new_1.extend(nums_1)

    temp = nums_2
    for i in range(2**n - 1):
        new_2.extend(temp)
        temp = Utils.DFF(temp, 1)

    # print(nums_1)
    # print(new_1)
    # print(nums_2)
    # print(new_2)

    return new_1, new_2



if __name__ == '__main__':
    simulate(6, [1, 2], [1, 2], 1, 1)
