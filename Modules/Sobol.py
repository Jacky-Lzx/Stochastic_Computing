import numpy
import sobol


def generate(dim: int, num: int):
    sample = sobol.sample(dim, num)
    # numpy.transpose(sample)
    # numpy.swapaxes(sample, 0, 1)
    # sample.transpose()
    sample = sample.T

    # return sample.tolist()
    return sample


if __name__ == '__main__':
    arr = generate(2, 5)
    print(arr)