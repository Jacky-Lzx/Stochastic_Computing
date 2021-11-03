from Modules import Utils
from Modules.LFSR import LFSR

if __name__ == '__main__':
    N = 8
    polynomial = [0, 1, 2, 5, 6]
    seed = [0 for _ in range(N)]
    seed[-1] = 1
    LEN = 2**N

    a_LFSR = LFSR(N, None)

    a_setting = LFSR.setting(seed, polynomial)

    nums = a_LFSR.simulate(a_setting)

    and_fn = lambda x, y: [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]

    MAE = 0
    y_sim = [0 for _ in range(LEN)]
    for x in range(LEN):
        bitstream_1 = Utils.comparator(nums, x, le=False)
        bitstream_2 = Utils.DFF(bitstream_1, 4)

        y_sim[x] = Utils.count_arr(and_fn(bitstream_1, bitstream_2)) / (LEN - 1)

        MAE += abs(y_sim[x] - x**2 / (LEN - 1)**2)

    MAE /= LEN

    from matplotlib import pyplot as pl

    x = range(LEN)
    y_real = [i**2 / (LEN - 1)**2 for i in x]
    # y_real = [i**2 for i in x]
    pl.plot(x, y_real)
    pl.plot(x, y_sim, '--')
    pl.show()

    print(y_real)
    print(y_sim)

    print(MAE)

    # print(and_fn(x1_bitstream, x2_bitstream))

    MAE = 0
    y_sim = [0 for _ in range(LEN)]
    for x in range(LEN):
        bitstream_1 = Utils.comparator(nums, x, le=True)
        bitstream_2 = Utils.DFF(bitstream_1, 4)

        y_sim[x] = Utils.count_arr(and_fn(bitstream_1, bitstream_2)) / (LEN - 1)
        # y_sim[x - 1] = Utils.count_arr(and_fn(bitstream_1, bitstream_2))

        MAE += abs(y_sim[x] - x**2 / (LEN - 1)**2)

    MAE /= (LEN - 1)

    from matplotlib import pyplot as pl

    x = range(LEN)
    y_real = [i**2 / (LEN - 1)**2 for i in x]
    # y_real = [i**2 for i in x]
    pl.plot(x, y_real)
    pl.plot(x, y_sim, '--')
    pl.show()

    print(y_real)
    print(y_sim)

    print(MAE)
