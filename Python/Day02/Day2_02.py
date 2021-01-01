# Problem: https://adventofcode.com/2020/day/2#part2

from pathlib import Path

def parse(s):

    password = s[1].strip()    

    val_letter = s[0].split(' ')
    val = val_letter[0].split('-')
    letter = val_letter[1]

    min_val = int(val[0])
    max_val = int(val[1])

    return(min_val, max_val, letter, password)

def check_valid(min_val, max_val, letter, password):     

    count = 0
    if password[min_val - 1] == letter:
        count = count + 1

    if password[max_val - 1] == letter:
        count = count + 1

    if count == 1:
        return True

    return False

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

with open(INPUT) as f:
    entries = list(map(lambda x: x.split(':'), f.readlines()))

count = 0
for entry in entries:
    min_val, max_val, letter, password = parse(entry)
    if check_valid(min_val, max_val, letter, password):
        count = count + 1

print(count)

# Result: 427