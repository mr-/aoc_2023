
def parse(lines):
    for line in lines:
        yield [int(x) for x in line.split()]

def diffsp(line):
    if all([x == 0 for x in line]):
        return []
    res = [a-b for a, b in zip(line, line[1:])]
    return [res] + diffsp(res)

def diffs(line):
    return list(reversed([line] + diffsp(line)))

def solve(ds):
    res = 0
    for a, b in zip(ds, ds[1:]):
        res = b[-1] - res
    return res

input = open("sample.txt").readlines()
input = open("input.txt").readlines()


lines = list(parse(input))

print(diffs(lines[0]))

s = sum([solve(diffs(line)) for line in lines])
print(s)
