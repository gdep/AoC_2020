# Problem: https://adventofcode.com/2020/day/1

from pathlib import Path

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

with open(INPUT) as f:
    entries = list(map(int, f.readlines()))
    
# Brute forcing it
for i in range(0, len(entries)):
    for j in range(i+1, len(entries)-1):
        if entries[i] + entries[j] == 2020:
            print(entries[i]*entries[j])

# Result: 211899