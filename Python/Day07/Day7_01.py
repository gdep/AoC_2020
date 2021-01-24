# Problem: https://adventofcode.com/2020/day/7

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

reverse_bag_map = {}
contained_list = []

def search_bags(start, bag_map, bag_list):
    if start in bag_map:
        init = bag_map[start]
    else:
        bag_list.append(start)
        return
    for bag in init:
        bag_list.append(bag)
        search_bags(bag, bag_map, bag_list)
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
                reverse_bag_map.setdefault(bag_color, []).append(contains)
    

search_bags('shiny gold', reverse_bag_map, contained_list)
print(len(set(contained_list)))

# Result: 139

