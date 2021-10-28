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

    N = 6

    # poly_1 = [4]
    # seed_1 = [0, 1, 0, 0, 0, 1]
    # scram_1 = (2, 0, 3, 5, 1, 4)
    # poly_1 = [4]
    # seed_1 = [0, 1, 0, 0, 0, 1]
    # scram_1 = (2, 0, 3, 5, 1, 4)
    poly_1 = [4]
    seed_1 = [0, 1, 0, 0, 0, 1]
    scram_1 = (2, 0, 3, 5, 1, 4)

    poly_2 = [4]
    seed_2 = [0, 1, 0, 0, 0, 1]
    scram_2 = (2, 0, 3, 5, 4, 1)

    # poly_2 = [0, 3, 4]
    # seed_2 = [1, 1, 1, 1, 0, 0]
    # scram_2 = (1, 3, 4, 0, 2, 5)

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

    # Random LFSRs
    polynomials = LFSR.search_polynomials(N)
    seeds = Utils.generate_seeding(N)
    scramblings = Utils.generate_scrambling(N)
    poly_rand_1 = polynomials[random.randint(0, len(polynomials) - 1)]
    poly_rand_2 = polynomials[random.randint(0, len(polynomials) - 1)]
    seed_rand_1 = seeds[random.randint(0, len(seeds) - 1)]
    seed_rand_2 = seeds[random.randint(0, len(seeds) - 1)]
    scram_rand_1 = scramblings[random.randint(0, len(scramblings) - 1)]
    scram_rand_2 = scramblings[random.randint(0, len(scramblings) - 1)]

    nums_rand_1 = LFSR.simulate(N, seed_rand_1, poly_rand_1, scram_rand_1)
    nums_rand_2 = LFSR.simulate(N, seed_rand_2, poly_rand_2, scram_rand_2)
    new_rand_1, new_rand_2 = Progress_core.rotate(N, nums_rand_1, nums_rand_2)
    MAEs_LFSR_rand = Progress_core.simulate(N, new_rand_1, new_rand_2, and_fn, real_fn)


    # Random Sobols
    random_times = 10
    sobols = Sobol.generate(random_times, LEN)
    sobol_nums_1 = sobols[random.randint(0, random_times - 1)]
    sobol_nums_2 = sobols[random.randint(0, random_times - 1)]
    sobol_new_1, sobol_new_2 = Progress_core.rotate(N, sobol_nums_1, sobol_nums_2)
    MAEs_Sobol = Progress_core.simulate(N, sobol_new_1, sobol_new_2, and_fn, real_fn)


    from matplotlib import pyplot as plt

    plt.plot(range(len(MAEs_LFSR)), MAEs_LFSR)
    plt.plot(range(len(MAEs_Sobol)), MAEs_Sobol)
    plt.plot(range(len(MAEs_LFSR_rand)), MAEs_LFSR_rand)
    # plt.ylim((0, 0.08))
    plt.legend(['LFSR', 'Sobol', 'LFSR rand'])
    plt.xlabel("n")
    plt.ylabel("MAE")
    plt.show()


