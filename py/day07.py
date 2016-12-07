#!/usr/bin/env python

def checkline(l):
    for c in zip(l[0:-3], l[1:-2], l[2:-1], l[3:]):
        if c[0] == c[3] and c[1] == c[2] and c[0] != c[1]:
            return True
    return False

def part1(s):
    import re

    n = 0
    for l in s:
        ll = re.split(r"[\[\]]", l)

        c = [checkline(lll) for lll in ll]

        if any(c[1::2]):
            continue
        elif any(c[::2]):
            n += 1

    return n

if __name__ == '__main__':
    import fileinput

    s = [l for l in fileinput.input()]
    print "part1:", part1(s)
