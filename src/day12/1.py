import re
import itertools

def strings(t, ns):
    N = len(t)
    n = sum(ns)
    gaps = len(ns) + 2
    rest = N - n
    candidates = range(1, rest-gaps+1)
    all_candidates = [candidates]*gaps
    return len([x for x in all_candidates if sum(x) <= rest])

def parse(line):
    template, rest = line.split()
    groups = list(map(int, rest.split(',')))


    return (template, groups)

def is_valid(ss, groups):
    s = ''.join(ss)
    hashes = re.split(r"\.+", s)
    actual = [len(h) for h in hashes]
    return groups == [a for a in actual if a != 0]

def generate(template, groups):
    hashes = sum(groups) - template.count("#")
    variables = template.count("?")
    products = itertools.product(*[["#", "."]] * variables)
    count = 0
    for p in products:
        # sanity check?
        if str(p).count("#") != hashes:
            continue

        t = list(template)
        i = 0
        for j in range(0, len(t)):
            if t[j] == '?':
                t[j] = p[i]
                i += 1
        if is_valid(t, groups):
            count += 1
    return count



tests = [
(("???.###", [1,1,3]), 1),
((".??..??...?##.", [1,1,3]), 4),
(("?#?#?#?#?#?#?#?", [1,3,1,6]), 1),
(("????.#...#...", [4,1,1]),  1),
(("????.######..#####.", [1,6,5]), 4),
(("?###????????", [3,2,1]), 10)
]


lines = open("sample.txt").readlines()
lines = open("input.txt").readlines()
parsed = [parse(line) for line in lines]

for test in tests:
    actual = generate(*test[0])
    expected = test[1] 
    print(f"actual: {actual}, expected: {expected}")
print(sum([generate(t, g) for t, g in parsed]))




#re.split(r"\.+", template)
