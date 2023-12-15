from collections import defaultdict
def parse(line):
    return line.strip().split(",")

def hash(s):
    r = 0
    for c in s:
        r += ord(c)
        r = r * 17
        r = r % 256
    return r

def index_where(l, pred):
    things = [i for i, e in enumerate(l) if pred(e)]
    if not things:
        return -1
    return things[0]

def pp(boxes):
    for k in sorted(boxes.keys()):
        print(f"{k}: {boxes[k]}")

line = open("sample.txt").readlines()[0]
line = open("input.txt").readlines()[0]
instructions = parse(line)

boxes = defaultdict(list)
for i in instructions:
    if "=" in i:
        label, focal = i.split("=")
        box_index = hash(label)
        box = boxes[box_index]
        fi = index_where(box, lambda x: x.startswith(f"{label}="))
        if fi > -1:
            box[fi] = i
        else:
            box.append(i)
    if "-" in i:
        label, *_ = i.split("-")
        box_index = hash(label)
        box = boxes[box_index]
        fi = index_where(box, lambda x: x.startswith(f"{label}="))
        if fi > -1:
            boxes[box_index] = box[:fi] + box[(fi+1):]

def focal_length(i):
    return int(i.split("=")[1])

s = 0
for k in boxes.keys():
    s += sum([(1+k) * (ind+1) * focal_length(inst) for ind, inst in enumerate(boxes[k])])

print(s)
