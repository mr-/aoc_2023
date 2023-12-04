import collections
import itertools




def neighbors(lines, m, y, x):
    l = len(m[y][x])
    c1 = [(y-1, dx) for dx in range(x-1, x+l+1)] 
    c2 = [(y, x-1), (y, x+l)] 
    c3 = [(y+1, dx) for dx in range(x-1, x+l+1)]
    candidates = c1 + c2 + c3

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
    res = []
    if m[y].get(x) is None:
        return res 
    if not isdigit(m[y][x]):
        return res 
#    print(f"checking {m[y][x]} at y={y} and x={x}")
    ns = neighbors(lines, m, y, x)
#    print(f"neighbors {ns}")
    for n in ns:
        cand = m[n[0]].get(n[1], '.')
        if cand == "*":
#            print(f"{m[y][x]} at y={y} and x={x}")
            res = res + [(n[0],n[1])]
    return res 

lines = open("sample.txt", "r").read().splitlines()
lines = open("input.txt", "r").read().splitlines()
things = parse(lines)

s = [((y,x), with_symbol(lines, things, y, x)) for y in range(0, len(lines)) for x in range(0, len(lines[0]))]

geared = [d for d in s if len(d[1]) > 0]

res = {}
for g in geared:
    for d in g[1]:
        res[d] = list(set(res.get(d, set())) | {g[0]})


relevant = [(res[k][0], res[k][1]) for k in res.keys() if len(res[k]) == 2]
print(relevant)
values = [(int(things[r[0][0]][r[0][1]]), int(things[r[1][0]][r[1][1]])) for r in relevant]
res = sum([x[0] * x[1] for x in values])
print(res)




