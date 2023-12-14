from itertools import takewhile 
def parse(lines):
    board = {}
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            c = lines[y][x]
            board[(x,y)] = c
    return board


lines = [line.strip() for line in open("input.txt").readlines()]
len_x = len(lines[0])
len_y = len(lines)
board = parse(lines)

def pp(board):
    for y in range(0, len_y):
        for x in range(0, len_x):
            print(board[(x,y)], end="")
        print()
    print()

def evaluate(board):
    s = 0
    for k in board.keys():
        if board[k] == "O":
            s += len_y - k[1] 

    return s


def tilt_north(board):
    for y in range(0, len_y):
        for x in range(0, len_x):
            if board[(x,y)] == "O":
                candidates = [((x, ny), board[(x,ny)]) for ny in reversed(range(0, y))]
                barrier = list(takewhile(lambda f: f[1] == ".", candidates))
                if len(barrier) == 0:
                    pass
                else:
                    b = barrier[-1]
                    board[(x,y)] = "."
                    board[b[0]] = "O"


tilt_north(board)
print(evaluate(board))
