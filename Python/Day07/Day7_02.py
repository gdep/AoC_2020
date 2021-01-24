# Problem: https://adventofcode.com/2020/day/7#part2

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

reverse_bag_map = {}
contained_list = []

def search_bags(start, bag_map, bag_list, multiplier):

    if start in bag_map:
        init = bag_map[start]
    else:
        return

    for bag in init:
        bag_list.append((bag[0]*multiplier, bag[1]))
        search_bags(bag[1], bag_map, bag_list, bag[0]*multiplier)

    return

with open(INPUT) as f:
    for line in f.readlines():

        m = re.match(r'(.*) bags contains? (.*)', line)

        contains = m.group(1)
        contained = m.group(2).split(',')

        if re.search(r'no other', contained[0], re.IGNORECASE) is None:
            contained = list(map(lambda x: re.sub(r'\sbags?\.?', '', x.strip()) ,contained))
            
            for bag in contained:
                split_bags = re.match(r'(\d+) ([\w|\s]+)', bag)
                n_bags = split_bags.group(1)
                bag_color = split_bags.group(2)
                reverse_bag_map.setdefault(contains, []).append((int(n_bags), bag_color))
    

search_bags('shiny gold', reverse_bag_map, contained_list,1)
print(sum([i[0] for i in contained_list]))

# Result: 58175

