# Problem: https://adventofcode.com/2020/day/8

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

instructions = {}
accumulator = 0
pos = 0

with open(INPUT) as f:
    for line in f.readlines():

        instruction_pre = line.split(' ')
        instruction = (instruction_pre[0], int(instruction_pre[1]), 0)
        instructions[pos] = instruction

        pos = pos + 1

pos = 0
while True:
    instruction = instructions[pos]
    if instruction[2] == 1:
        break
    elif instruction[0] == 'acc':
        accumulator += instruction[1]
        instructions[pos] = (instruction[0], instruction[1], 1)
        pos += 1
    elif instruction[0] == 'nop':
        instructions[pos] = (instruction[0], instruction[1], 1)
        pos += 1
    elif instruction[0] == 'jmp':
        instructions[pos] = (instruction[0], instruction[1], 1)
        pos += instruction[1]

print(accumulator)

# Result: 1087

