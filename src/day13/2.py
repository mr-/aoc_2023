from itertools import product

def parse_block(lines):
    return list(lines.splitlines())

def parse(fn):
    blocks = open(fn).read().split('\n\n')
    return [parse_block(block) for block in blocks]

def vertical_mirrorss(block):
    for y in range(1, len(block)):
        mirrors = True
        for x in range(0, len(block[y])):
            left = [b[x] for b in block[:y]]
            right = [b[x] for b in block[y:]]
            if any(a != b for a,b in zip(reversed(left), right)):
                mirrors = False
        if mirrors:
            yield y
def vertical_mirrors(block):
    return list(vertical_mirrorss(block))

def horizontal_mirrorss(block):
    for x in range(1, len(block[0])):
        mirrors = True
        for y in range(0, len(block)):
            left = block[y][:x]
            right = block[y][x:]
            if any(a != b for a,b in zip(reversed(left), right)):
                mirrors = False
        if mirrors:
            yield x

def horizontal_mirrors(block):
    return list(horizontal_mirrorss(block))

def flip(block, rx, ry):
    for y in range(0, len(block)):
        if y != ry:
            yield block[y]
        else:
            c = '.' if block[y][rx] == "#" else "#"
            yield "".join(list(block[y][:rx]) + [c] + list(block[y][rx+1:]))

def pp(block):
    print("\n".join(block))

def do(block):
    v = vertical_mirrors(block)
    h = horizontal_mirrors(block)
    for x,y in product(range(0, len(block[0])), range(0, len(block))):
        flipped = list(flip(block, x, y))
        fv = vertical_mirrors(flipped)
        fh = horizontal_mirrors(flipped)
        if fv != [] and fv != v:
            return 100 * list(set(fv)- set(v))[0] 
        if fh != [] and fh != h:
            return list(set(fh)- set(h))[0] 

blocks = parse("sample.txt")
blocks = parse("input.txt")


print(sum(do(block) for block in blocks))


