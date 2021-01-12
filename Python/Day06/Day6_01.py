# Problem: https://adventofcode.com/2020/day/6

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

yes_quests = set()
running_total = 0

with open(INPUT) as f:
    for line in f.readlines():
        print(running_total)

        if line.strip() == "":
            running_total += len(yes_quests)
            yes_quests = set()
        else:
            for item in list(line.strip()):
                yes_quests.add(item) 
    
    running_total += len(yes_quests)


        
print(running_total)
    
# Result: 7110

