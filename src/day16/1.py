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

lines = [l.strip() for l in open("sample.txt").readlines()]
lines = [l.strip() for l in open("input.txt").readlines()]
board = parse(lines)

seen = set()
seen.add(((0,0), "right"))
follow(board, (0,0), "right", seen)

actual ={s[0] for s in seen}
pp(lines, actual)

print(len(actual))
