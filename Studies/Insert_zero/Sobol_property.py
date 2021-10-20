from Modules import Sobol
from Modules import Utils

from matplotlib import pyplot as plt

if __name__ == '__main__':
    N = 8
    LEN = 2**N
    sobol_nums = Sobol.generate(1, LEN)
    sobol_nums = Utils.DFF(sobol_nums, 1)
    print(sobol_nums)
    plt.plot(range(LEN - 1), sobol_nums, 'o')
    plt.show()

