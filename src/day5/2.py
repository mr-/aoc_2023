
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def parse_seeds(input):
    _, *seeds = input.split()
    for chunk in chunks(seeds, 2):
        yield {"start": int(chunk[0]), "range": int(chunk[1])}

def parse_map_line(input):
    out, iin, r = input.split()
    return {"in": int(iin), "out": int(out), "range": int(r)}

def parse_map(input):
    _, *lines = input.splitlines()
    return [parse_map_line(line) for line in lines]


def parse(input):
    seeds, *maps = input.split("\n\n")
    return {
        "seeds": list(parse_seeds(seeds)),
        "maps": [parse_map(map) for map in maps]
    }

def evaluate(mapping, input):
    for map_line in mapping:
        if map_line["in"] <= input and input < (map_line["in"] + map_line["range"]):
            diff = (input - map_line["in"])
            res = map_line["out"] + diff 
            return res
    return input


# strategy, split the input range on the (repaired) map ranges, so that
# we can use the old evaluate on the parts.

def split_range(map_lines, input):
    gaps = get_map_gaps(map_lines, input)
    lines = map_lines + gaps
    check_map_gaps(lines)
    ranges = []
    for line in lines:
        map_lower = line["in"]
        map_upper = line["in"] + line["range"]

        in_lower = input["start"]
        in_upper = input["start"] + input["range"]

        if not (map_lower > in_upper or map_upper < in_lower):
            inter_lower = max(map_lower, in_lower)
            inter_upper = min(map_upper, in_upper)
            ranges.append({
                "start": inter_lower, 
                "range": inter_upper - inter_lower})

    return ranges


# Analysis says: We have gaps, but no overlaps.
def check_map_gaps(map_lines):
    sorted_lines = sorted(map_lines, key=lambda m: m["in"])
    for (a,b) in zip(sorted_lines, sorted_lines[1:]):
        exp = b["in"]
        act = a["in"] + a["range"]
        if act != exp:
            print(f"WOAH left={a['in']} right={exp} {act<exp}")

def get_map_gaps(map_lines, input):
    gaps = []
    sorted_lines = sorted(map_lines, key=lambda m: m["in"])
    for (a,b) in zip(sorted_lines, sorted_lines[1:]):
        exp = b["in"]
        act = a["in"] + a["range"]
        if act < exp:
            gap = {"in": act, "out": act, "range": exp - act}
            gaps.append(gap)
        elif act > exp:
            print("WTF!")

    map_min = sorted_lines[0]["in"]
    if input["start"] < map_min:
        gaps.append({
            "in": input["start"], 
            "out": input["start"], 
            "range": map_min - input["start"]})


    map_max = sorted_lines[-1]["in"] + sorted_lines[-1]["range"]
    input_max = input["start"] + input["range"]
    if  map_max < input_max:
        gaps.append({
            "in": map_max, 
            "out": map_max, 
            "range": input_max - map_max})
    return gaps

def validate(seed, inputs):
    inputs = sorted(inputs, key=lambda x: x["start"])
    s = seed["start"] == inputs[0]["start"]
    e = (seed["start"] + seed["range"]) == (inputs[-1]["start"] + inputs[-1]["range"])
    if not (s and e):
        print("wrong inputs..")

    for (a,b) in zip(inputs, inputs[1:]):
        if not (a["start"] + a["range"] == b["start"]):
            print("gaps in input")

def ev(map, inputs):
    res = []
    for seed in inputs:
        new_input = split_range(map, seed)
        print(sorted(new_input, key=lambda x: x["start"]))
        validate(seed, new_input)
        res += [{"start": evaluate(map, i["start"]), "range": i["range"]} for i in new_input]
    return res

input = open("sample.txt", "r").read()
input = open("sample2.txt", "r").read()

input = open("input.txt", "r").read()
parsed = parse(input)

res = parsed["seeds"]

for map in parsed["maps"]:
    res = ev(map, res)

print(min(res, key=lambda x: x["start"]))


