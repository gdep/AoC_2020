# Problem: https://adventofcode.com/2020/day/10#part2

from pathlib import Path
from functools import lru_cache

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

jolts = []

# Changed to lru_cache after seeing better implementations
@lru_cache(16)
def split_sum(jolts, curr):
    path = jolts[1:]
    # If diff <= 3, continue adding
    if jolts[0] - curr <= 3:
        # If its the end of the path, return adding 1
        if not path:
            return 1
        else: 
            return (
                split_sum(path, jolts[0]) + split_sum(path, curr)
            )
    # No more paths left, diff > 3
    else:
        return 0

with open(INPUT) as f:
    for line in f.readlines():
        jolts.append(int(line))

    jolts.sort()

print(split_sum(tuple(jolts), 0))

# Result: 86812553324672


