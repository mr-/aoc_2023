
def parse(line):
    id, nrs, *_ = line.split(':')
    card, guesses, *_ = nrs.split('|')
    card_numbers = filter(lambda x: x != '', card.split(" "))
    guess_numbers = filter(lambda x: x != '', guesses.split(" "))

    _, id, *_ = id.split()

    return {
        "id": int(id), 
        "card": set(map(int, card_numbers)), 
        "guesses": set(map(int, guess_numbers)),
        "count": 1}


input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17 9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

lines = input.splitlines()
lines = open("input.txt", "r").read().splitlines()

def matches(game):
    return len(game["card"] & game["guesses"])

parsed = [parse(line) for line in lines]
parsed = {x["id"]:x for x in parsed}


for i in range(1, len(lines)):
    game = parsed[i]
    wins = matches(game)
    for w in range(1, wins+1):
        if i + w < len(lines):
            parsed[i+w]["count"] += game["count"]


print(sum([p["count"] for p in parsed.values()]))
