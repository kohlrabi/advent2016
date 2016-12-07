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

def checkline2(l):
    import re
    matches = []
    for c in zip(l[0:-2], l[1:-1], l[2:]):
        if c[0] == c[2]:
            matches.append("".join((c[1], c[0], c[1])))
    return matches

def part2(s):
    import re

    n = 0
    for l in s:
        ll = re.split(r"[\[\]]", l)

        gl = [checkline2(lll) for lll in ll[::2]]

        
        found = False
        for gll in gl:
            for m in gll:
                for bl in ll[1::2]:
                    if m in bl and not found:
                        n += 1
                        found = True
    
    return n

if __name__ == '__main__':
    import fileinput

    s = [l for l in fileinput.input()]
    print "part1:", part1(s)
    print "part2:", part2(s)
