# Problem: https://adventofcode.com/2020/day/5#part2

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

ids = []

with open(INPUT) as f:
    for line in f.readlines():
        row = line[:7]
        column = line[7:]

        row_value = int(row.replace('B', '1').replace('F', '0'), 2)
        col_value = int(column.replace('R', '1').replace('L', '0'), 2)
        seat_id = (row_value * 8) + col_value
        ids.append(seat_id)


my_id = 0
for id in range(min(ids), max(ids)):
    if ((id - 1) in ids) and ((id + 1) in ids) and (id not in ids):
        my_id = id


print(my_id)
    
# Result: 515

