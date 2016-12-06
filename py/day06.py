#!/usr/bin/env python

import fileinput
import collections

s = [l for l in fileinput.input()]

def part1(s):
    t = zip(*s)[:-1]
    r = [collections.Counter(tt).most_common(1)[0] for tt in t]
    ret = "".join([rr[0] for rr in r])
    return ret

print "part 1:", part1(s)

