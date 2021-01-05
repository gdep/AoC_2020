# Problem: https://adventofcode.com/2020/day/3

from pathlib import Path


INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

with open(INPUT) as f:
    slope = f.readlines()

pos = 0
tree_counter = 0

for line in slope:
    if line[pos] == '#':
        tree_counter = tree_counter + 1
    
    pos = (pos + 3) % (len(line)-1)

print(tree_counter)


# Result: 181