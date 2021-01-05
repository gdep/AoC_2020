# Problem: https://adventofcode.com/2020/day/3#part2

from pathlib import Path

def down_slope(slope, step_x, step_y):

    pos_x = 0    
    tree_counter = 0        

    for pos_y in range(0, len(slope), step_y):
        
        if slope[pos_y][pos_x] == '#':
            tree_counter = tree_counter + 1
            
        pos_x = (pos_x + step_x) % (len(slope[:][pos_y])-1)        

    return tree_counter

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

with open(INPUT) as f:
    slope = f.readlines()

print(down_slope(slope, 1, 1), down_slope(slope, 3, 1), down_slope(slope, 5, 1), down_slope(slope, 7, 1), down_slope(slope, 1, 2))
print(down_slope(slope, 1, 1) * down_slope(slope, 3, 1) * down_slope(slope, 5, 1) * down_slope(slope, 7, 1) * down_slope(slope, 1, 2))


# Result: 1260601650