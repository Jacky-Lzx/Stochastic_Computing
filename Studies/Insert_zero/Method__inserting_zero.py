from Modules import LFSR, Utils

if __name__ == '__main__':
    N = 8
    polynomials = LFSR.search_polynomials(N)
    # polynomial = polynomials[0]
    seed = [0 for _ in range(N)]
    seed[-1] = 1
    LEN = 2**N

    MAE_1s = list()
    MAE_2s = list()

    for polynomial in polynomials:
        nums_1 = LFSR.simulate(N, seed, polynomial)
        nums_2 = Utils.DFF(nums_1, 4)
        nums_3 = LFSR.simulate(N, seed, polynomial, None, 100)
        nums_4 = Utils.DFF(nums_3, 4)

        and_fn = lambda x, y: [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]

        MAE_1 = 0
        y_sim_1 = [0 for _ in range(LEN)]
        for x in range(LEN):
            output = and_fn(Utils.comparator(nums_1, x, le=True), Utils.comparator(nums_2, x, le=True))
            y_sim_1[x] = Utils.count_arr(output) / (LEN - 1)

            MAE_1 += abs(y_sim_1[x] - x**2 / (LEN - 1)**2)

        MAE_1 /= LEN
        print(f"MAE_1: {MAE_1}")
        MAE_1s.append(MAE_1)

        MAE_2 = 0
        y_sim_2 = [0 for _ in range(LEN)]
        for x in range(LEN):
            output = and_fn(Utils.comparator(nums_3, x, le=False), Utils.comparator(nums_4, x, le=False))
            y_sim_2[x] = Utils.count_arr(output) / LEN

            MAE_2 += abs(y_sim_2[x] - x**2 / LEN**2)

        MAE_2 /= LEN
        print(f"MAE_2: {MAE_2}")
        MAE_2s.append(MAE_2)

    from matplotlib import pyplot as plt

    plt.plot(range(len(MAE_1s)), MAE_1s)
    plt.plot(range(len(MAE_2s)), MAE_2s)
    plt.xlabel("polynomial")
    plt.ylabel("MAE")
    plt.legend(["no zero", "insert zero"])
    plt.show()
