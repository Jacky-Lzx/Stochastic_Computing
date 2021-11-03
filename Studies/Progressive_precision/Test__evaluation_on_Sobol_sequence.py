import Evaluate_function__point_distribution
import Progress_core
from Modules import Sobol
if __name__ == '__main__':
    sobol_num = 10
    N = 5
    LEN = 2**N
    sobol_sequences = Sobol.generate(sobol_num, LEN)
    for sobol_sequence in sobol_sequences:
        _, sobol_sequence_rotate = Progress_core.rotate(None, sobol_sequence)
        ret = Evaluate_function__point_distribution.evaluate_3(N, sobol_sequence_rotate)
        print(sobol_sequence)
        print(ret)
