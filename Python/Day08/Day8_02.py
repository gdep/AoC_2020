# Problem: https://adventofcode.com/2020/day/8#part2

from pathlib import Path
import re

INPUT = str(Path(__file__).parent.absolute()) + '/input.txt'

def run_instructions(instructions):

    accumulator = 0
    pos = 0
    end = False

    while not end:
        instruction = instructions[pos]
        if instruction[2] == 1:
            break
        elif (pos == len(instructions)-1 and pos != 'jmp'):
            end = True
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

    return accumulator, end

instructions = {}
pos = 0

with open(INPUT) as f:
    for line in f.readlines():

        instruction_pre = line.split(' ')
        instruction = (instruction_pre[0], int(instruction_pre[1]), 0)
        instructions[pos] = instruction

        pos = pos + 1

# Brute forcing...
for i in range(len(instructions)):
    pos = 0
    accumulator = 0
    run = True
    new_instructions = instructions.copy()
    if instructions[i][0] == 'jmp':
        new_instructions[i] = ('nop', instructions[i][1], instructions[i][2])
    elif instructions[i][0] == 'nop':
        new_instructions[i] = ('jmp', instructions[i][1], instructions[i][2])

    res, end = run_instructions(new_instructions)
    if end:
        break

print(res)

# Result: 1087

