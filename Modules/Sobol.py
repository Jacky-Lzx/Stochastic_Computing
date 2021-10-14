import numpy
import sobol


def generate(dim: int, num: int):
    sample = sobol.sample(dim, num)
    # numpy.transpose(sample)
    # numpy.swapaxes(sample, 0, 1)
    # sample.transpose()
    sample = sample.T

    # return sample.tolist()
    return sample.tolist()


if __name__ == '__main__':
    arr_0, arr_1 = generate(2, 5)
    print(type(arr_0))
    print(arr_1)
