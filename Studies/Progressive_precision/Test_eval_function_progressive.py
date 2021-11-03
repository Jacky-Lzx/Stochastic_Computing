from Modules import Utils, Sobol
from Modules.LFSR import LFSR
import Progress_core

if __name__ == '__main__':
    # N = 4
    # seed_1 = [1,0,1,0]
    # poly_1 = [0]
    # scram_1 = (3,0,1,2)
    #
    # seed_2 = [0, 1, 0, 1]
    # poly_2 = [2]
    # scram_2 = (2, 0, 1, 3)

    N = 7
    poly_1 = [0, 3, 5]
    seed_1 = [0, 0, 0, 0, 1, 1, 1]
    scram_1 = (4, 1, 6, 3, 2, 0, 5)

    poly_2 = [0, 1, 3, 4, 5]
    seed_2 = [0, 0, 1, 0, 0, 0, 1]
    scram_2 = (0, 1, 6, 2, 5, 3, 4)

    LEN = 2**N
    a_LFSR = LFSR(N)

    def and_fn(x, y): return [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    def real_fn(x): return x**2 / LEN**2

    setting_1 = LFSR.setting(seed_1, poly_1, scram_1, None, True, 0)
    nums_1 = a_LFSR.simulate(setting_1)
    print(f"length of nums_1: {len(nums_1)}")
    setting_2 = LFSR.setting(seed_2, poly_2, scram_2, None, True, 0)
    nums_2 = a_LFSR.simulate(setting_2)
    print(f"length of nums_2: {len(nums_2)}")
    new_1, new_2 = Progress_core.rotate(nums_1, nums_2)
    print(f"length of new_1: {len(new_1)}")
    MAEs_LFSR = Progress_core.simulate(N, new_1, new_2, and_fn, real_fn, le=False)

    N = 6
    LEN = 2**N
    sobol_nums_1, sobol_nums_2 = Sobol.generate(2, LEN)
    sobol_new_1, sobol_new_2 = Progress_core.rotate(sobol_nums_1, sobol_nums_2)
    MAEs_Sobol = Progress_core.simulate(N, sobol_new_1, sobol_new_2, and_fn, real_fn, le=False)

    from matplotlib import pyplot as plt
    plt.plot(range(len(MAEs_LFSR[1:])), MAEs_LFSR[1:])
    plt.plot(range(len(MAEs_Sobol)), MAEs_Sobol)
    # plt.ylim((0, 0.08))
    plt.legend(['7-bit LFSR', '6-bit Sobol'])
    plt.xlabel("n")
    plt.ylabel("MAE")
    plt.show()


