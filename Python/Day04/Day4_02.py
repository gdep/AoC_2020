# Problem: https://adventofcode.com/2020/day/4#part2

from pathlib import Path
import re

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

        valid = True

        byr = int(re.search('byr:(\\d+)(?:\\Z|\\s)', passport).group(1))
        if (byr < 1920 or byr > 2002):
            valid = False

        iyr = int(re.search('iyr:(\\d+)(?:\\Z|\\s)', passport).group(1))
        if (iyr < 2010 or iyr > 2020):
            valid = False

        eyr = int(re.search('eyr:(\\d+)(?:\\Z|\\s)', passport).group(1))
        if (eyr < 2020 or eyr > 2030):
            valid = False

        hgt = re.search('hgt:(.*?)(?:\\Z|\\s)', passport).group(1)
        measure_type = re.search('(in|cm)', hgt)
        measure_val = re.search('(\\d+)[in|cm]', hgt)

        if measure_type is None:
            valid = False
        elif ((measure_type.group(1) == 'cm' and (int(measure_val.group(1)) < 150 or int(measure_val.group(1)) > 193)) or 
             (measure_type.group(1) == 'in' and (int(measure_val.group(1)) < 59 or int(measure_val.group(1)) > 76))):            
            valid = False

        hcl = re.search('hcl:(.*?)(?:\\Z|\\s)', passport).group(1)
        if not re.match('\\A#[a-f0-9]{6}\\Z', hcl):
            valid = False

        ecl = re.search('ecl:(.*?)(?:\\Z|\\s)', passport).group(1)
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False

        pid = re.search('pid:(.*?)(?:\\Z|\\s)', passport).group(1)
        if not re.match('\\A[0-9]{9}\\Z', pid):
            valid = False

        if valid:
            print(hcl)

            print('Valid')
            valid_total += 1

print(valid_total)

# Result: 233