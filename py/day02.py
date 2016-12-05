#!/usr/bin/env python

def part1(s):
    num = 5
    r = ""

    moves = {
            'U': lambda x: -3 * (x > 3),
            'D': lambda x: 3 * (x < 7),
            'L': lambda x: -1 * (x%3 != 1),
            'R': lambda x: 1 * (x%3 != 0)
            }

    for l in s:
        for c in l.strip():
            num += moves[c](num)
        r += str(num)

    return r


if __name__ == '__main__':
    import fileinput

    s = [l for l in fileinput.input()]

    print "part 1:", part1(s)






