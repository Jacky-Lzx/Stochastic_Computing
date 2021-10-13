

if __name__ == '__main__':
    """ The absolute MAE caused by multiplication """
    N = 8
    LEN = 2**N

    """" f(x, y) = x * y """
    absolute_MAE = 0
    # Traverse from 0 to 2^N - 1
    for i in range(LEN):
        for j in range(LEN):
            x = round((i * j) / (LEN - 1))
            absolute_MAE += abs(x / (LEN - 1) - (i * j) / (LEN - 1)**2)
    absolute_MAE /= LEN**2
    print(absolute_MAE)

    """" f(x) = x^2 """
    absolute_MAE = 0
    for i in range(LEN):
        x = round((i * i) / (LEN - 1))
        absolute_MAE += abs(x / (LEN - 1) - (i * i) / (LEN - 1)**2)
    absolute_MAE /= LEN
    print(absolute_MAE)
