input = open("sample.txt", "r").read()
input = open("input.txt", "r").read()

def parse_seeds(input):
    _, *seeds = input.split()
    return list(map(int, seeds))

def parse_map_line(input):
    out, iin, r = input.split()
    return {"in": int(iin), "out": int(out), "range": int(r)}

def parse_map(input):
    _, *lines = input.splitlines()
    return [parse_map_line(line) for line in lines]


def parse(input):
    seeds, *maps = input.split("\n\n")
    return {
        "seeds": parse_seeds(seeds),
        "maps": [parse_map(map) for map in maps]
    }

def evaluate(mapping, input):
#    print(f"Ev {mapping} {input}")
    for map_line in mapping:
        if map_line["in"] <= input and input <= (map_line["in"] + map_line["range"]):
            diff = (input - map_line["in"])
            res = map_line["out"] + diff 
#            print(f"found: {map_line} matches {input} with diff {diff} and result {res}")
            return res
    return input


parsed = parse(input)
print(parsed)
evaluate(parsed["maps"][0], 79)

reses = []
for seed in parsed["seeds"]:
    res = seed
    for map in parsed["maps"]:
        res = evaluate(map, res)
#        print(res)
#    print(res)
    reses.append(res)


print(min(reses))
