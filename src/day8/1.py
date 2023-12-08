import re
from itertools import cycle

def parse(fn):
    instructions, _, *defs = open(fn).readlines()
    tree = [parse_line(line) for line in defs]
    tree = {x["id"]:x for x in tree}
    return {"tree": tree, "path": instructions.strip()}

def parse_line(line):
    m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
    this, left, right = m.groups()
    return {"id": this, "L": left, "R": right}

parsed = parse("sample.txt")
parsed = parse("sample2.txt")
parsed = parse("input.txt")
print(parsed)

tree = parsed["tree"]
node = "AAA"
c = 0

for dir in cycle(parsed["path"]):
    c += 1
    print(node)
    print(dir)
    node = tree[node][dir]

    if node == "ZZZ":
        print(c)
        exit()
