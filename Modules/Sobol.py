from typing import List

import numpy
import sobol


def generate(dim: int, num: int) -> List[List[int]]:
    sample = sobol.sample(dim, num - 1)
    # numpy.transpose(sample)
    # numpy.swapaxes(sample, 0, 1)
    # sample.transpose()
    # sample = numpy.insert(sample, 0, 0, axis=0)

    sample = sample.T
    sample *= num


    # return sample.tolist()
    return sample.tolist()[0] if dim == 1 else sample.tolist()


if __name__ == '__main__':
    arr_0, arr_1 = generate(2, 8)
    print(arr_0)
    print(arr_1)
