from functools import cache

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
    groups = tuple(map(int, rest.split(',')))


    return (template, groups)


def explode(template, groups):
    return ("?".join([template]*5), groups*5)

@cache
def count_solutions(template, groups, in_progress=0):
    if not groups:
#        print("ran out of groups")
        if template.find("#") >= 0:
            return 0
        else:
#            print(f"{sol} {template}")
            return 1
    if not template:
#        print("ran out of template")
        if not groups or (len(groups)==1 and groups[0] == in_progress):
#            print(f"{sol} {groups} {in_progress}")
            return 1
        else:
#            print(f"but still got {groups}")
            return 0
    choices = ["#", "."] if template[0] == "?" else [template[0]]
    res = 0
#    print(f"CHOICE {template} {groups} {in_progress}")
    for c in choices:
        if c == "#":
            # can we have a # here?
            if in_progress < groups[0]:
                # only if group is still "open"
#                print("  adding a #")
                res += count_solutions(template[1:], groups, in_progress+1)
#            else:
#                print(f"   could not add spring to {template} with {groups}")
        if c == ".":
            # can we have a "." here?
            if in_progress == 0:
#                print("    Nothing in progress, allowing . here")
                res += count_solutions(template[1:], groups, 0)
            elif in_progress == groups[0]:
#                print("   Group is done, allowing . here")
                res += count_solutions(template[1:], groups[1:], 0)
#            else:
#                print(f"   could not add period to {template} with {groups}")
    return res



tests = [
(("???.###", (1,1,3)), 1),
((".??..??...?##.", (1,1,3)), 4),
(("?#?#?#?#?#?#?#?", (1,3,1,6)), 1),
(("????.#...#...", (4,1,1)),  1),
(("????.######..#####.", (1,6,5)), 4),
(("?###????????", (3,2,1)), 10)
]


lines = open("sample.txt").readlines()
lines = open("input.txt").readlines()
parsed = [parse(line) for line in lines]
parsed = [explode(*p) for p in parsed]

print(sum([count_solutions(t, g) for t, g in parsed]))

