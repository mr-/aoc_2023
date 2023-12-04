
def parse(line):
    _, nrs, *_ = line.split(':')
    card, guesses, *_ = nrs.split('|')
    card_numbers = filter(lambda x: x != '', card.split(" "))
    guess_numbers = filter(lambda x: x != '', guesses.split(" "))
    return(set(map(int, card_numbers)), set(map(int, guess_numbers)))


input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17 9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

lines = input.splitlines()
lines = open("input.txt", "r").read().splitlines()

def ev(game):
    i = len(game[0] & game[1])
    if i == 0:
        return 0

    return pow(2, i-1)

s = sum([ev(parse(line)) for line in lines])
print(s)
