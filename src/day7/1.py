import collections
def normalize(s):
    d = {
        'A': 'm', 
        'K': 'l', 
        'Q': 'k', 
        'J': 'j', 
        'T': 'i',
        '9': 'h', 
        '8': 'g', 
        '7': 'f', 
        '6': 'e', 
        '5': 'd', 
        '4': 'c',
        '3': 'b', 
        '2': 'a'} 
    return ''.join([d[c] for c in s])

def rank(s):
    cnts = collections.defaultdict(int) 
    for c in s:
        cnts[c] += 1

    ks = str(cnts.values())
    if '5' in ks:
        return 6
    if '4' in ks: 
        return 5
    if '3' in ks and '2' in ks:
        return 4
    if '3' in ks:
        return 3
    if ks.count('2') == 2:
        return 2
    if ks.count('2') == 1:
        return 1
    return 0

def to_key(s):
    return str(rank(s)) + normalize(s)

def parse(lines):
    for l in lines:
        hand, bid = l.split()
        yield {"hand":hand, "bid":int(bid)} 

def test_thing():
    order_sample = """AAAAA
    AA8AA
    23332
    TTT98
    23432
    A23A4
    23456"""
    print("keys")
    print([to_key(e) for e in order_sample.splitlines()])
    
    foo = list(sorted(order_sample.splitlines(), key=to_key))
    print("sorted")
    print(foo)



lines = open("input.txt").readlines()
#lines = open("sample.txt").readlines()

hands = parse(lines)

s = list(sorted(hands, key=lambda l: to_key(l["hand"])))
zipped = list(zip(s, range(1, len(s)+3))) 
for x, i in zipped:
    print(f"{x['hand']} -> {to_key(x['hand'])} : {x['bid']} {i}")

print(sum([h["bid"] * i for h, i in zipped]))
