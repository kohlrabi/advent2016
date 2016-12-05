#!/usr/bin/env python

import fileinput

s = [l for l in fileinput.input()]

def part1(s):
    num = 5
    r = ""

    moves = {
            'U': lambda x: -3 if x > 3 else 0,
            'D': lambda x: 3 if x < 7 else 0,
            'L': lambda x: -1 if x%3 != 1 else 0,
            'R': lambda x: 1 if x%3 != 0 else 0
            }

    for l in s:
        for c in l.strip():
            num += moves[c](num)
        r += str(num)

    return r

print "part 1:", part1(s)






