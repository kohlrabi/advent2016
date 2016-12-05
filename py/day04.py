#!/usr/bin/env python

import fileinput

s = [l for l in fileinput.input()]

def part1(s):
    import collections
    import itertools
    import operator

    ret = 0
    
    for l in s:
        d = collections.defaultdict(lambda: 0)
        sl = l.split('-')
        for ssl in sl[:-1]:
            for c in ssl:
                d[c] += 1
        check = sl[-1][-7:-2]
        idd = int(sl[-1].split('[')[0])

        ss = sorted(d.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True)
        r = "".join([sss[0] for sss in ss[:5]])

        if r == check:
            ret += idd 

    return ret

def rot(s, n=0):
    n %= 26
    r = []
    for l in s:
        b = [ord(c) for c in l]
        b = [bb + n for bb in b]
        b = [bb - 26 * (bb > 122) for bb in b]
        r.append("".join([chr(i) for i in b]))
    return r

def part2(s):

    for l in s:
        sl = l.split('-')
        idd = int(sl[-1].split('[')[0])
        r = rot(sl[:-1], idd)
        r = " ".join(r)
        if r == "northpole object storage":
            return idd
    return 0

print "part 1:", part1(s)
print "part 2:", part2(s)
