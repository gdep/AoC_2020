# Problem: https://adventofcode.com/2020/day/10

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

jolts = [0]

with open(INPUT) as f:
    for line in f.readlines():
        jolts.append(int(line))

    jolts.sort()

counts = {1:0, 2:0, 3:1}

for i in range(1, len(jolts)):
    counts[jolts[i] - jolts[i-1]] += 1

print(counts[1] * counts[3])

# Result: 1836


