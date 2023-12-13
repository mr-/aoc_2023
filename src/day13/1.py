
def parse(fn):
    blocks = open(fn).read().split('\n\n')
    return [list(block.splitlines()) for block in blocks]

def vertical_mirror(block):
    for y in range(1, len(block)):
        mirrors = True
        for x in range(0, len(block[y])):
            left = [b[x] for b in block[:y]]
            right = [b[x] for b in block[y:]]
            if any(a != b for a,b in zip(reversed(left), right)):
                mirrors = False
        if mirrors:
            return y

def horizontal_mirror(block):
    for x in range(1, len(block[0])):
        mirrors = True
        for y in range(0, len(block)):
            left = block[y][:x]
            right = block[y][x:]
            if any(a != b for a,b in zip(reversed(left), right)):
                mirrors = False
        if mirrors:
            return x

def flip(block, rx, ry):
    for y in range(0, len(block)):
        if y != ry:
            yield block[y]
        else:
            c = '.' if block[y][rx] == "#" else "#"
            yield "".join(list(block[y][:rx]) + [c] + list(block[y][rx+1:]))

blocks = parse("sample.txt")
blocks = parse("input.txt")

s = 0
for block in blocks:
    v = vertical_mirror(block)
    h = horizontal_mirror(block)
    s += 100 * v if v is not None else 0
    s += h if h is not None else 0

print(s)
