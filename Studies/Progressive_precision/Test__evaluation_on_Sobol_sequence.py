import Evaluate_function__point_distribution
import Progress_core
from Modules import Sobol
if __name__ == '__main__':
    N = 5
    LEN = 2**N
    sobol_sequence = Sobol.generate(1, LEN)
    sobol_sequence[0:0] = [0]
    _, sobol_sequence_rotate = Progress_core.rotate(N, None, sobol_sequence)
    ret = Evaluate_function__point_distribution.evaluate_2(N, sobol_sequence_rotate)
    print(sobol_sequence)
    print(ret)
