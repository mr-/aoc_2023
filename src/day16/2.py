# remember energized tiles and direction they were energized from.
import sys
sys.setrecursionlimit(100000)

def parse(lines):
    board = {}
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
                c = lines[y][x]
                board[(x,y)] = c
    return board

def follow(board, pos, dir, seen):
    down = ((0,1), "down")
    right = ((1,0), "right")
    left = ((-1,0), "left")
    up = ((0,-1), "up")
    next = {
        "right": {
            "\\": [down],
            "-": [right],
            ".": [right],
            "/": [up],
            "|": [down, up],
        },
        "left": {
            "\\": [up],
            "-": [left],
            ".": [left],
            "/": [down],
            "|": [down, up]
        },
        "up": {
            "\\": [left],
            "-": [left, right],
            "/": [right],
            "|": [up],
            ".": [up]
        },
        "down": {
            "\\": [right],
            "-": [left, right],
            "/": [left],
            "|": [down],
            ".": [down]
        }
        
    }
    followups = next[dir][board[pos]]

    for d, new_dir in followups:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if (new_pos, new_dir) in seen:
            continue 
        if not new_pos in board:
            continue 
        seen.add((new_pos, new_dir))
        follow(board, new_pos, new_dir, seen)

def pp(lines, seen):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if (x, y) in seen:
                print("#", end="")
            else:
                print(".", end="")
        print()

def do(board, p, dir):
    seen = set()
    seen.add((p, dir))
    follow(board, p, dir, seen)
    actual = {s[0] for s in seen}
    return len(actual)

lines = [l.strip() for l in open("sample.txt").readlines()]
lines = [l.strip() for l in open("input.txt").readlines()]
board = parse(lines)

a = [do(board, (0, y), "right") for y in range(0, len(lines))]
b = [do(board, (len(lines[0])-1, y), "left") for y in range(0, len(lines))]
c = [do(board, (x, 0), "down") for x in range(0, len(lines[0]))]
d = [do(board, (x, len(lines)-1), "up") for x in range(0, len(lines[0]))]

print(max(a + b + c + d))
