from Modules import Utils

def MAE_simulate(n: int, nums_1: list, nums_2: list, circuit_fn, real_fn, le: bool = False) -> float:
    MAE = 0
    LEN = 2**n
    len_arr = len(nums_1)
    y_sim = [0 for _ in range(LEN)]
    for x in range(LEN):
        output = circuit_fn(Utils.comparator(nums_1, x, le), Utils.comparator(nums_2, x, le))
        y_sim[x] = Utils.count_arr(output) / len_arr

        MAE += abs(y_sim[x] - real_fn(x))

    MAE /= LEN

    return MAE
