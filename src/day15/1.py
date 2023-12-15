def parse(line):
    return line.strip().split(",")

def hash(s):
    r = 0
    for c in s:
        r += ord(c)
        r = r * 17
        r = r % 256
    return r


line = open("input.txt").readlines()[0]
s = sum([hash(inst) for inst in parse(line)])

print(s)

