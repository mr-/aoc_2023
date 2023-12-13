

def parse(lines):
    res = {}
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                res[(x,y)] = "#"
    return res

def gslice(x=None, y=None):
    if not x is None:
        return [p for p in galaxy.keys() if p[0] == x]
    if not y is None:
        return [p for p in galaxy.keys() if p[1] == y]

def get_doublings(galaxy):
    maxx = max(galaxy.keys(), key=lambda p: p[0])[0]
    maxy = max(galaxy.keys(), key=lambda p: p[1])[1]
    hd = []
    for x in range(0, maxx+1):
        if len(gslice(x=x)) == 0:
            hd.append(x)

    vd = []
    for y in range(0, maxy+1):
        if len(gslice(y=y)) == 0:
            vd.append(y)
    return {"vert": vd, "hor": hd}

def expand(galaxy, doublings, fact=1):
    res = {}
    for p in galaxy.keys():
        dx = len([x for x in doublings["hor"] if x < p[0] ]) * fact 
        dy = len([y for y in doublings["vert"] if y < p[1] ]) * fact 
        res[(p[0] + dx, p[1] + dy)] = "#"
    return res

def distances(galaxy):
    res = {}
    for p in galaxy.keys():
        for q in galaxy.keys():
            (a,b) = (p,q) if p < q else (q,p)
            res[(a,b)] = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return res


lines = open("input.txt").readlines()
galaxy = parse(lines)


print(galaxy)
doublings = get_doublings(galaxy)
galaxy = expand(galaxy, doublings, fact=999999)

ds = distances(galaxy)
print(sum(ds.values()))

