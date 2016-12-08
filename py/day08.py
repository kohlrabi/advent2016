#!/usr/bin/env python

import numpy
 
class screen(object):

    def __init__(self, rows=6, cols=50):
        self.d = numpy.zeros((rows, cols), dtype=bool)

    def rect(self, A, B):
        self.d[:B, :A] = 1

    def rot(self, A, B, row=True):
        if row:
            self.d[A] = numpy.roll(self.d[A], B)
        else:
            self.d[:,A] = numpy.roll(self.d[:,A], B)

    def rot_row(self, A, B):
        self.rot(A, B, row=True)
    
    def rot_col(self, A, B):
        self.rot(A, B, row=False)

    def sum(self):
        return self.d.sum()


def part1(s):
    import re
    
    r = re.compile("(\d+)")

    sc = screen()

    for l in s:
        A, B = [int(x) for x in r.findall(l)]
        if "rect" in l:
            sc.rect(A, B)
        if "row" in l:
            sc.rot_row(A, B)
        if "column" in l:
            sc.rot_col(A, B)

    return sc

def part2(s):
    d = part1(s).d

    s = "\n"
    for i in d:
        s += "".join(['#' if x else ' ' for x in i])
        s += "\n"

    return s[:-1]
    

if __name__ == '__main__':
    import fileinput

    s = [x for x in fileinput.input()]

    print "part1:", part1(s).sum()
    print "part2:", part2(s)

