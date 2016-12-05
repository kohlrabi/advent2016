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

print "part 1:", part1(s)




