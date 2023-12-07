import collections
def normalize(s):
    d = {
        'A': 'm', 
        'K': 'l', 
        'Q': 'k', 
        'J': 'J', 
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

def pre_rank(s):
    cnts = collections.defaultdict(int) 
    for c in s:
        cnts[c] += 1

    max_c = max(cnts.items(), key=lambda v: v[1])[0]

    ks = str(cnts.values())
    if '5' in ks:
        return (6, max_c)
    if '4' in ks: 
        return (5, max_c)
    if '3' in ks and '2' in ks:
        return (4, max_c)
    if '3' in ks:
        return (3, max_c)
    if ks.count('2') == 2:
        return (2, max_c)
    if ks.count('2') == 1:
        return (1, max_c)
    return (0, max_c)

def rank(s):
    new_s = s.replace('J', '')
    if new_s == '':
        return 6
    pr = pre_rank(new_s)

    newer_s = s.replace('J', pr[1])
    return pre_rank(newer_s)[0]

def to_key(s):
    return str(rank(s)) + normalize(s)

def parse(lines):
    for l in lines:
        hand, bid = l.split()
        yield {"hand":hand, "bid":int(bid)} 


lines = open("input.txt").readlines()
#lines = open("sample.txt").readlines()

hands = parse(lines)

s = list(sorted(hands, key=lambda l: to_key(l["hand"])))
zipped = list(zip(s, range(1, len(s)+3))) 
for x, i in zipped:
    print(f"{x['hand']} -> {to_key(x['hand'])} : {x['bid']} {i}")

print(sum([h["bid"] * i for h, i in zipped]))
