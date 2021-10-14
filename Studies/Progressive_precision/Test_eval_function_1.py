from Modules import LFSR, Utils

if __name__ == '__main__':
    N = 6
    LEN = 2**N

    seed_1 = [0, 1, 0, 0, 0, 1]
    poly_1 = [4]
    scram_1 = (2, 0, 3, 5, 1, 4)
    nums_1 = LFSR.simulate(N, seed_1, poly_1, scram_1)

    seed_2 = [0, 1, 1, 0, 0, 0]
    poly_2 = [0, 3, 4]
    scram_2 = (0, 3, 2, 1, 4, 5)
    nums_2 = LFSR.simulate(N, seed_2, poly_2, scram_2)

    and_fn = lambda x, y: [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]

    MAE = 0
    y_sim = [0 for _ in range(LEN)]
    for x in range(LEN):
        bitstream_1 = Utils.comparator(nums_1, x, le=False)
        # bitstream_2 = Utils.DFF(bitstream_1, 4)
        bitstream_2 = Utils.comparator(nums_2, x, le=False)

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
        bitstream_1 = Utils.comparator(nums_1, x, le=True)
        # bitstream_2 = Utils.DFF(bitstream_1, 4)
        bitstream_2 = Utils.comparator(nums_2, x, le=True)

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
