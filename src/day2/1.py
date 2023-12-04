import re

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

lines = open("input.txt", "r").readlines()
# lines = input.splitlines()

def parse_game(game):
    res = {}
    ms = re.findall(r'(\d+) (\w+)', game)
    for m in ms:
        res[m[1]] = int(m[0])

    return res

def parse(line):
    print(line)
    id, games, *_ = line.split(":")
    _, id, *_ = id.split(" ")
    games = games.split(";")


    return {"id": int(id), "games": [parse_game(game) for game in games]}


bag = {"red": 12, "green": 13, "blue": 14}


def satisfies(bag, game):
    for b in bag.keys():
        if game.get(b, 0) > bag[b]:
            return False
    return True

def all_satisfy(bag, g):
    return all([satisfies(bag, game) for game in g["games"]])

parsed = [parse(line) for line in lines]
print(sum([game["id"] for game in parsed if all_satisfy(bag, game)]))


