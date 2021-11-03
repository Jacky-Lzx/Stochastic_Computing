from typing import List


class LFSR_2:
    def __init__(self, N: int, inverter: List[int] = None):
        self.N = N
        if inverter is not None:
            assert len(inverter) == N
        self.inverters = inverter

    def simulate(self, setting):
        pass


if __name__ == '__main__':
    pass