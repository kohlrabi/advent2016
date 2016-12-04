#!/usr/bin/env python
dirs = raw_input().split(',')
locs = []
loc = 0j
dir = 1
hq = False
locs += [loc]
for d in dirs:
    dd = d.strip()
    dir *= 1j if dd[0]=='L' else -1j
    for i in xrange(int(dd[1:])):
        loc += dir
        if loc in locs and not hq:
            print "part 2:", int(abs(loc.real) + abs(loc.imag))
            hq = True
        locs.append(loc)
print "part 1:", int(abs(locs[-1].real) + abs(locs[-1].imag))
