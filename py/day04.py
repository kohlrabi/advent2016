import fileinput

s = [l for l in fileinput.input()]

def part1(s):
    import collections
    import itertools

    ret = 0
    
    for l in s:
        ok = True
        d = collections.defaultdict(lambda: 0)
        sl = l.split('-')
        for ssl in sl[:-1]:
            for c in ssl:
                d[c] += 1
        check = sl[-1][-7:-2]
        idd = int(sl[-1].split('[')[0])
        dd = [d[c] for c in check]
        
        for i in sorted(d.values())[::-1]:
            if 
            if dd[i] < dd[i+1]:
                ok = False
            elif dd[i] == dd[i+1] and ord(check[i]) > ord(check[i+1]):
                    ok = False

        ret += idd * ok

    return ret


print "part 1", part1(s)




