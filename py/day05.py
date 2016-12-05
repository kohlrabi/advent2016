#!/usr/bin/env python
inp = "abbhdwsy"

def part1(inp):
    import hashlib

    ret = ""
    i = 0
    while(len(ret) < 8):
        h = hashlib.md5(inp + str(i)).hexdigest()
        i += 1
        if h[:5] == '00000':
            ret += h[5]

    return ret

def part2(inp):
    import hashlib

    ret = ['x']*8
    i = 0
    while(ret.count('x') > 0):
        h = hashlib.md5(inp + str(i)).hexdigest()
        i += 1
        if h[:5] == '00000':
            pos = int(h[5],16)
            if pos < 8 and ret[pos] == 'x':
                ret[pos] = h[6]

    return "".join(ret)


if __name__ == '__main__':
    print "part1:", part1(inp)
    print "part2:", part2(inp)
