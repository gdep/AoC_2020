# Problem: https://adventofcode.com/2020/day/9

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

def subset_sum(arr, target):
    
    seq = []
    total = 0
    for i in range(0, len(arr)):
        if total < target:
            seq.append(arr[i])
            total += arr[i]
        if total == target and len(seq) >= 2:
            return seq
        while total > target:
            total -= seq.pop(0)
            
    return

transmission = []

with open(INPUT) as f:
    for line in f.readlines():
        transmission.append(int(line))

target = 57195069
res = subset_sum(transmission, target)

print(min(res) + max(res))

# Result: 7409241


