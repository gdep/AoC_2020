# Problem: https://adventofcode.com/2020/day/4

from pathlib import Path


INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

passports = []

with open(INPUT) as f:
    tmp = ""
    for line in f.readlines():
        if(line.strip() == ""):
            passports.append(tmp.strip())
            tmp = ""
        else:
            tmp = tmp + " " + line.strip()

    passports.append(tmp.strip())

valid_total = 0

for passport in passports:

    if (passport.count(':') == 8) or (passport.count(':') == 7 and (passport.count('cid:') == 0)):
        valid_total += 1

print(valid_total)

# Result: 233