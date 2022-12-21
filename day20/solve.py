#!/usr/local/bin/python3
from cycledlist import CycledList


def go_right(node, repeats):
    current = node
    for i in range(repeats):
        current = current.next

    return current


def go_left(node, repeats):
    current = node
    for i in range(abs(repeats)):
        current = current.prev

    return current


def mix(numbers, sequence):
    for n in numbers:
        if n == 0:
            continue
        current = sequence.find(n)
        if n < 0:
            new_current = go_left(current, n)
            sequence.put_before(new_current, n)
        else:
            new_current = go_right(current, n)
            sequence.put_after(new_current, n)

        sequence.delete(current)


with open('./input2.txt') as f:
    numbers = list(map(int, f.read().splitlines()))

    sequence = CycledList()
    sequence.from_array(numbers.copy())
    mix(numbers, sequence)
    seq_arr = sequence.to_array()

    zero = seq_arr.index(0)
    one = seq_arr[(zero + 1000) % len(seq_arr)]
    two = seq_arr[(zero + 2000) % len(seq_arr)]
    three = seq_arr[(zero + 3000) % len(seq_arr)]

    print(one, two, three)
    print(one + two + three)

