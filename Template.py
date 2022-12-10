from time import perf_counter as pfc

def read_puzzle(file):
    with open(file) as f:
        return None


def solve(puzzle):
    return None
    


start=pfc()
print(solve(read_puzzle("DayXX.txt")))
print(pfc()-start)
