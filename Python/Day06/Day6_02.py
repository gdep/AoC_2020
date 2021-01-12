# Problem: https://adventofcode.com/2020/day/6#part2

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

yes_quests = set()
quests_list = []
running_total = 0

with open(INPUT) as f:
    for line in f.readlines():

        if line.strip() == "":
            every_yes = quests_list[0]
            for s in quests_list:
                every_yes = every_yes & s

            running_total += len(every_yes)
            quests_list = []
        else:
            for item in list(line.strip()):
                yes_quests.add(item) 

            quests_list.append(yes_quests)
            yes_quests = set()
    
    running_total += len(yes_quests)

print(running_total)
    
# Result: 3628

