# Problem: https://adventofcode.com/2020/day/5

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

max_id = 0

with open(INPUT) as f:
    for line in f.readlines():
        row = line[:7]
        column = line[7:]

        row_value = int(row.replace('B', '1').replace('F', '0'), 2)
        col_value = int(column.replace('R', '1').replace('L', '0'), 2)
        seat_id = (row_value * 8) + col_value
        if seat_id > max_id:
            max_id = seat_id 

print(max_id)
    
# Result: 930

