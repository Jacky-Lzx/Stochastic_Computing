import random

from Modules import Utils, Sobol
from Modules.LFSR import LFSR
import Progress_core

from matplotlib import pyplot as plt

if __name__ == '__main__':
    # N = 4

    N = 5

    file_polys = list()
    file_seeds = list()
    file_scrams = list()
    with open("Evaluate_function_3_result_n=5_inserting_zero.txt") as in_file:
        lines = in_file.readlines()
        for line in lines:
            if line.startswith("poly"):
                # file_polys.append(line[5:-1])
                file_polys.append([int(a) for a in line[7:-2].split(", ")])
            elif line.startswith("seed"):
                file_seeds.append([int(a) for a in line[7:-2].split(", ")])
            elif line.startswith("scram"):
                file_scrams.append(tuple([int(a) for a in line[8:-2].split(", ")]))

    LEN = 2**N

    def and_fn(x, y): return [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    def real_fn(x): return x**2 / LEN**2

    a_LFSR = LFSR(N)
    for i in range(5):
        rand_1 = 0
        rand_2 = 0
        while file_polys[rand_1] == file_polys[rand_2]:
            rand_1 = random.randint(0, len(file_seeds) - 1)
            rand_2 = random.randint(0, len(file_seeds) - 1)

        seed_1, seed_2 = file_seeds[rand_1], file_seeds[rand_2]
        poly_1, poly_2 = file_polys[rand_1], file_polys[rand_2]
        scram_1, scram_2 = file_scrams[rand_1], file_scrams[rand_2]

        setting_1 = LFSR.setting(seed_1, poly_1, scram_1, None, True, 0)
        nums_1 = a_LFSR.simulate(setting_1)
        setting_2 = LFSR.setting(seed_2, poly_2, scram_2, None, True, 0)
        nums_2 = a_LFSR.simulate(setting_2)
        new_1, new_2 = Progress_core.rotate(nums_1, nums_2)
        MAEs_LFSR = Progress_core.simulate(N, new_1, new_2, and_fn, real_fn)
        print(f"{i}'s random: {MAEs_LFSR}")
        plt.plot(range(len(MAEs_LFSR)), MAEs_LFSR, 'b')

    # Random LFSRs
    polynomials = a_LFSR.search_polynomials()
    seeds = Utils.generate_seeding(N)
    scramblings = Utils.generate_scrambling(N)
    for i in range(5):
        rand_1 = 0
        rand_2 = 0
        while polynomials[rand_1] == polynomials[rand_2]:
            rand_1 = random.randint(0, len(polynomials) - 1)
            rand_2 = random.randint(0, len(polynomials) - 1)

        poly_rand_1 = polynomials[rand_1]
        poly_rand_2 = polynomials[rand_2]
        seed_rand_1 = seeds[rand_1]
        seed_rand_2 = seeds[rand_2]
        scram_rand_1 = scramblings[rand_1]
        scram_rand_2 = scramblings[rand_2]

        setting_3 = LFSR.setting(seed_rand_1, poly_rand_1, scram_rand_1, None, True, 0)
        nums_rand_1 = a_LFSR.simulate(setting_3)
        setting_4 = LFSR.setting(seed_rand_2, poly_rand_2, scram_rand_2, None, True, 0)
        nums_rand_2 = a_LFSR.simulate(setting_4)
        new_rand_1, new_rand_2 = Progress_core.rotate(nums_rand_1, nums_rand_2)
        MAEs_LFSR_rand = Progress_core.simulate(N, new_rand_1, new_rand_2, and_fn, real_fn)
        print(f"Random LFSR: {MAEs_LFSR_rand}")
        plt.plot(range(len(MAEs_LFSR_rand)), MAEs_LFSR_rand, 'r')

    # Random Sobols
    # random_times = 10
    # sobols = Sobol.generate(random_times, LEN)
    # sobol_nums_1 = sobols[random.randint(0, random_times - 1)]
    # sobol_nums_2 = sobols[random.randint(0, random_times - 1)]
    # sobol_new_1, sobol_new_2 = Progress_core.rotate(sobol_nums_1, sobol_nums_2)
    # MAEs_Sobol = Progress_core.simulate(N, sobol_new_1, sobol_new_2, and_fn, real_fn)
    #
    # print(f"Sobol: {MAEs_Sobol}")

    # from matplotlib import pyplot as plt
    # plt.plot(range(len(MAEs_LFSR)), MAEs_LFSR)
    # plt.plot(range(len(MAEs_Sobol)), MAEs_Sobol)
    # plt.plot(range(len(MAEs_LFSR_rand)), MAEs_LFSR_rand)
    # plt.ylim((0, 0.08))
    # plt.legend(['LFSR', 'LFSR rand'])
    plt.xlabel("n")
    plt.ylabel("MAE")
    plt.show()

