#!/usr/local/bin/python3
import re
import collections

REGEXP = r"(\w+) (\d+) (\w+) (\d+) (\w+) (\d+)"

def move(stacks, from_index, to_index, quantity):
    for i in range(quantity):
        el = stacks[from_index].pop()
        stacks[to_index].append(el)


def move_same_order(stacks, from_index, to_index, quantity):
    stack_tmp = []
    for i in range(quantity):
        el = stacks[from_index].pop()
        stack_tmp.append(el)
    while len(stack_tmp) > 0:
        el = stack_tmp.pop()
        stacks[to_index].append(el)

with open('./input.txt') as f:
    lines = f.read().splitlines()
    stacks_a = collections.defaultdict(lambda: [])
    stacks_b = collections.defaultdict(lambda: [])

    empty_index = lines.index('')
    stack_input = lines[0:empty_index - 1]
    move_input = lines[empty_index + 1:]

    for line in stack_input:
        print(line)
        groups = re.match(r"(\s{4}|(\[[A-Z]\]{1}))", line).
        print(groups, len(groups))
        print('---')
