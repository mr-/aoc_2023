import re
from itertools import cycle
from collections import defaultdict
from functools import reduce

def parse(fn):
    instructions, _, *defs = open(fn).readlines()
    tree = [parse_line(line) for line in defs]
    tree = {x["id"]:x for x in tree}
    return {"tree": tree, "path": instructions.strip()}

def parse_line(line):
    m = re.match(r"(\w+) = \((\w+), (\w+)\)", line)
    this, left, right = m.groups()
    return {"id": this, "L": left, "R": right}


def starts(nodes):
    return [node for node in nodes if node.endswith("A")]

def detect_cycle(tree, instructions, start):
    node = start
    path = [start]
    seen = defaultdict(set) 
    for dir, i in cycle(zip(instructions, range(0, len(instructions)))):
        node = tree[node][dir]
        path.append(node)
        if i in seen[node]:
            s = path.index(node)
            cycle_len = len(path) - s - 1
            print(f"{start}: Found cycle starting at {s} with {node} and has length {cycle_len}")
            zs_in_path = [x for x in zip(range(0, len(path)), path) if x[1].endswith('Z')]
            # In our dataset, there's only one z in the cycle..
            z = zs_in_path[-1]
            print(f"Equation is i * {cycle_len} + {z[0]}")
            yield (cycle_len, z[0])
            return
        seen[node].add(i)


def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(args):
    return reduce(lcm, args)



#Idea: 
# Figure out their cycles.
# Record when in their cycle they are at a Z
# That will give some equations like cycle_len_1*n + offset
# which describe the position of the zs in the path
# i.e. the list of indices of zs in the path.
# Then we can find a common element in all the lists for all the starting points.
# math help us all


#parsed = parse("sample.txt")
#parsed = parse("sample2.txt")
parsed = parse("sample3.txt")
parsed = parse("input.txt")


tree = parsed["tree"]
nodes = starts(tree.keys())
eqsp = [detect_cycle(tree, parsed["path"], node) for node in nodes] 
eqs = [x[0] for y in eqsp for x in y]

# XSA: Found cycle starting at 2 with TRC and has length 16409
# Equation is i * 16409 + 16409
# VVA: Found cycle starting at 2 with SLR and has length 12643
# Equation is i * 12643 + 12643
# TTA: Found cycle starting at 4 with RJM and has length 21251
# Equation is i * 21251 + 21251
# AAA: Found cycle starting at 5 with HHB and has length 15871
# Equation is i * 15871 + 15871
# NBA: Found cycle starting at 2 with VQR and has length 19637
# Equation is i * 19637 + 19637
# MHA: Found cycle starting at 2 with LGH and has length 11567
# Equation is i * 11567 + 11567

# We are lucky, the equations are literally just x*cycle_len, so the lcm comes to the rescue

print(lcmm(eqs))
#sol: 11283670395017


