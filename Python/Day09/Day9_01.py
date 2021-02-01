# Problem: https://adventofcode.com/2020/day/9

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

preample = 25

def is_sum(arr, value):
    found = False
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if arr[i] + arr[j] == value:
                found = True
                break

    return found

transmission = []

with open(INPUT) as f:
    for line in f.readlines():
        transmission.append(int(line))

for i in range(preample, len(transmission)):
    found = is_sum(transmission[i-preample:i], transmission[i])
    if not found:
        break

print(transmission[i])

# Result: 57195069


