import fileinput
import numpy

s = [l for l in fileinput.input()]
s = [[int(ll) for ll in l.split()] for l in s]
s = numpy.array(s)

def part1(s):
    a,b,c = s.T
    n = (a + b > c) * (a + c > b) * (b + c > a)
    return n.sum()

def part2(s):
    ss = numpy.reshape(s.T, (-1,3))
    return part1(ss)

print "part1:", part1(s)
print "part2:", part2(s)

