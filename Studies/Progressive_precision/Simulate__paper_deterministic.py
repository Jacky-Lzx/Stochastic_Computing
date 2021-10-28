import random
from typing import List
from Modules import Utils
from Modules import Sobol
from Modules import LFSR
import Progress_core


def counter(n: int) -> List[int]:
    ans = list()
    for i in range(2**n):
        temp_bits = Utils.num_to_arr(n, i)
        temp_bits.reverse()
        ans.append(temp_bits)
    # print(ans)
    return Utils.bit_arrays_to_nums(n, ans)[1:]
    # return Utils.bit_arrays_to_nums(n, ans)


def sobol_source_2(n: int) -> List[int]:
    rand_num = 10
    sobols = Sobol.generate(rand_num, 2**n)
    ans = sobols[random.randint(0, rand_num - 1)]
    # ans.insert(0, 0)
    return ans


if __name__ == '__main__':
    N = 5

    poly_1 = [1]
    seed_1 = [0, 0, 0, 0, 1]
    scram_1 = (0, 1, 2, 3, 4)

    poly_2 = [1, 2, 3]
    seed_2 = [1, 0, 1, 1, 0]
    scram_2 = (4, 0, 3, 1, 2)

    LEN = 2**N
    and_fn = lambda x, y: [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    real_fn = lambda x: x**2 / (LEN - 1)**2

    sobol_1 = counter(N)
    sobol_2 = sobol_source_2(N)
    sobol_rotate_1, sobol_rotate_2 = Progress_core.rotate(N, sobol_1, sobol_2)
    MAEs = Progress_core.simulate(N, sobol_rotate_1, sobol_rotate_2, and_fn, real_fn, True)

    nums_1 = LFSR.simulate(N, seed_1, poly_1, scram_1)
    nums_2 = LFSR.simulate(N, seed_2, poly_2, scram_2)
    new_1, new_2 = Progress_core.rotate(N, nums_1, nums_2)
    MAEs_LFSR = Progress_core.simulate(N, new_1, new_2, and_fn, real_fn, True)

    from matplotlib import pyplot as plt
    plt.plot(range(2*N + 1), MAEs)
    plt.plot(range(2*N + 1), MAEs_LFSR)
    plt.legend(["Sobol", "LFSR"])
    plt.show()
