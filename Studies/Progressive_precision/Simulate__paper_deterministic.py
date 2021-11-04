import random
from typing import List
from Modules import Utils
from Modules import Sobol
from Modules.LFSR import LFSR
import Progress_core


def counter(n: int) -> List[int]:
    ans = list()
    for i in range(2**n):
        temp_bits = Utils.num_to_arr(n, i)
        temp_bits.reverse()
        ans.append(temp_bits)
    # print(ans)
    # return Utils.bit_arrays_to_nums(n, ans)[1:]
    return Utils.bit_arrays_to_nums(n, ans)


def sobol_source_2(n: int) -> List[int]:
    rand_num = 10
    sobols = Sobol.generate(rand_num, 2**n)
    ans = sobols[random.randint(0, rand_num - 1)]
    # ans.insert(0, 0)
    return ans


if __name__ == '__main__':
    N = 5

    poly_1 = [1]
    seed_1 = [1, 1, 1, 0, 1]
    scram_1 = (0, 1, 4, 2, 3)

    poly_2 = [2]
    seed_2 = [1, 0, 1, 1, 1]
    scram_2 = (4, 3, 0, 2, 1)

    LEN = 2**N
    def and_fn(x, y): return [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    def real_fn(x): return x**2 / LEN**2

    sobol_1 = counter(N)
    sobol_2 = sobol_source_2(N)
    sobol_rotate_1, sobol_rotate_2 = Progress_core.rotate(sobol_1, sobol_2)
    MAEs = Progress_core.simulate(N, sobol_rotate_1, sobol_rotate_2, and_fn, real_fn, False)

    a_LFSR = LFSR(N)
    setting_1 = LFSR.setting(seed_1, poly_1, scram_1, None, True, 0)
    nums_1 = a_LFSR.simulate(setting_1)
    setting_2 = LFSR.setting(seed_2, poly_2, scram_2, None, True, 0)
    nums_2 = a_LFSR.simulate(setting_2)
    new_1, new_2 = Progress_core.rotate(nums_1, nums_2)
    MAEs_LFSR = Progress_core.simulate(N, new_1, new_2, and_fn, real_fn, False)

    from matplotlib import pyplot as plt
    plt.plot(range(2*N + 1), MAEs)
    plt.plot(range(2*N + 1), MAEs_LFSR)
    plt.legend(["Sobol", "LFSR"])
    plt.show()
