from Modules import LFSR, Utils
import Progress_core

if __name__ == '__main__':
    N = 4
    LEN = 2**N

    seed_1 = [1,0,1,0]
    poly_1 = [0]
    scram_1 = (3,0,1,2)
    nums_1 = LFSR.simulate(N, seed_1, poly_1, scram_1)

    seed_2 = [0, 1, 0, 1]
    poly_2 = [2]
    scram_2 = (2, 0, 1, 3)
    nums_2 = LFSR.simulate(N, seed_2, poly_2, scram_2)

    and_fn = lambda x, y: [1 if (x[i] == 1 and y[i] == 1) else 0 for i in range(len(x))]
    real_fn = lambda x: x**2 / (LEN - 1)**2

    new_1, new_2 = Progress_core.rotate(N, nums_1, nums_2)

    Progress_core.simulate(N, new_1, new_2, and_fn, real_fn)
