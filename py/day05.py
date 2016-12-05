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
            if len(ret) == 8:
                break

    return ret

if __name__ == '__main__':
    print "part1:", part1(inp)
