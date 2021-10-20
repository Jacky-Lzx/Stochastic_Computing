import random

from Modules import LFSR, Utils, Sobol
import Progress_core

if __name__ == '__main__':
    # N = 4
    # seed_1 = [0, 1, 0, 1]
    # poly_1 = [0]
    # scram_1 = (3, 0, 1, 2)
    #
    # seed_2 = [0, 1, 0, 1]
    # poly_2 = [2]
    # scram_2 = (3, 0, 2, 1)

    N = 5

    # poly_1 = [4]
    # seed_1 = [0, 1, 0, 0, 0, 1]
    # scram_1 = (2, 0, 3, 5, 1, 4)
    poly_1 = [1]
    seed_1 = [0, 0, 0, 0, 1]
    scram_1 = (0, 1, 2, 3, 4)

    poly_2 = [1, 2, 3]
    seed_2 = [1, 0, 1, 1, 0]
    scram_2 = (4, 0, 3, 1, 2)
    # N = 7
    # poly_1 = [0, 3, 5]
    # seed_1 = [0, 0, 0, 0, 1, 1, 1]
    # scram_1 = (4, 1, 6, 3, 2, 0, 5)
    #
    # poly_2 = [0, 1, 3, 4, 5]
    # seed_2 = [0, 0, 1, 0, 0, 0, 1]
    # scram_2 = (0, 1, 6, 2, 5, 3, 4)

    LEN = 2**N

    and_fn = lambda x, y: [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    real_fn = lambda x: x**2 / (LEN - 1)**2

    nums_1 = LFSR.simulate(N, seed_1, poly_1, scram_1)
    nums_2 = LFSR.simulate(N, seed_2, poly_2, scram_2)
    new_1, new_2 = Progress_core.rotate(N, nums_1, nums_2)
    MAEs_LFSR = Progress_core.simulate(N, new_1, new_2, and_fn, real_fn)

    random_times = 10
    N = 5
    LEN = 2**N
    sobols = Sobol.generate(random_times, LEN)
    sobol_nums_1 = sobols[random.randint(0, random_times - 1)]
    sobol_nums_2 = sobols[random.randint(0, random_times - 1)]
    sobol_new_1, sobol_new_2 = Progress_core.rotate(N, sobol_nums_1, sobol_nums_2)
    MAEs_Sobol = Progress_core.simulate(N, sobol_new_1, sobol_new_2, and_fn, real_fn)


    from matplotlib import pyplot as plt

    plt.plot(range(len(MAEs_LFSR)), MAEs_LFSR)
    plt.plot(range(len(MAEs_Sobol)), MAEs_Sobol)
    # plt.ylim((0, 0.08))
    plt.legend(['LFSR', 'Sobol'])
    plt.xlabel("n")
    plt.ylabel("MAE")
    plt.show()


