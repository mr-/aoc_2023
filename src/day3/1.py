import collections
import itertools




def neighbors(lines, m, y, x):
    l = len(m[y][x])
    c1 = [(y-1, dx) for dx in range(x-1, x+l+1)] 
    print(c1)
    c2 = [(y, x-1), (y, x+l)] 
    print(c2)
    c3 = [(y+1, dx) for dx in range(x-1, x+l+1)]
    print(c3)
    candidates = c1 + c2 + c3
    print(f"len(m) = {len(m)}, len(m[0]) = {len(m[0])}")

    # this is (y,x)
    return [d for d in candidates if d[0] <= len(lines) and d[1] <= len(lines[0]) and d[0] >= 0  and d[1] >= 0]


def parse(lines):
    things = collections.defaultdict(dict)
    for y in range(0, len(lines)):
        x = 0
        while x < len(lines[0]):
            c = lines[y][x]
            if c.isdigit():
                nr = list(itertools.takewhile(lambda x: x.isdigit(), lines[y][x:]))
                things[y][x] = ''.join(nr)
                x = x + len(nr)
            elif not c == '.':
                things[y][x] = c
                x += 1
            else:
                things[y][x] = '.' 
                x += 1
    return things

def pp(things, lines):
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            print(things[y].get(x, ""), end="")
        print()

def isdigit(s):
    return all([c.isdigit() for c in s])


def with_symbol(lines, m, y, x):
    if m[y].get(x) is None:
        return False
    if not isdigit(m[y][x]):
        return False
    print(f"checking {m[y][x]} at y={y} and x={x}")
    ns = neighbors(lines, m, y, x)
    print(f"neighbors {ns}")
    for n in ns:
        cand = m[n[0]].get(n[1], '.')
        if not(cand == '.' or isdigit(cand)):
            print(f"{m[y][x]} at y={y} and x={x}")
            return True
    return False

#lines = open("sample.txt", "r").read().splitlines()
lines = open("input.txt", "r").read().splitlines()
things = parse(lines)
pp(things, lines)

s = sum([int(things[y][x]) for y in range(0, len(lines)) for x in range(0, len(lines[0])) if with_symbol(lines, things, y, x)])
print(s)



