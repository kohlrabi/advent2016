#!/usr/bin/env python

def part1(s):
    import hashlib
    import re

    n = 0
    marker = None
    while(True):
        p = s.find('(')
        if p == -1:
            n += len(s)
            break
        n += p
        s = s[p:]
        e = s.find(')')
        marker = [int(x) for x in re.split("x",s[1:e])]
        n += marker[0]*marker[1]
        s = s[e+1+marker[0]:]

    return n

def part2(s):
    return 


if __name__ == '__main__':
    import fileinput
    s = [i for i in fileinput.input()][0][:-1]

    print "part1:", part1(s)
    print "part2:", part2(s)
