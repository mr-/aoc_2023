from itertools import takewhile 
def parse(lines):
    board = {}
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            c = lines[y][x]
            board[(x,y)] = c
    return board

class hashabledict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


lines = open("input.txt").readlines()

lines = [line.strip() for line in lines]
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
    nb = board.copy() 
    for y in range(0, len_y):
        for x in range(0, len_x):
            if nb[(x,y)] == "O":
                candidates = [((x, ny), nb[(x,ny)]) for ny in reversed(range(0, y))]
                barrier = list(takewhile(lambda f: f[1] == ".", candidates))
                if len(barrier) == 0:
                    pass
                else:
                    b = barrier[-1]
                    nb[(x,y)] = "."
                    nb[b[0]] = "O"
    return nb

def rotate_board(board):
    nb = {}
    for k in board.keys():
        nb[(len_x-1 - k[1], k[0])] = board[k]
    return nb

def cycle(board):
    board = tilt_north(board)
    board = rotate_board(board)                

    board = tilt_north(board)
    board = rotate_board(board)                
    
    board = tilt_north(board)
    board = rotate_board(board)                
    
    board = tilt_north(board)
    board = rotate_board(board)

    return board

def find_cycle(board):
    seen = {}
    for i in range(0, 10000):
        nb = cycle(board)
        hb = hashabledict(nb)
        if hb in seen:
            print(f"first: {seen[hb]} now: {i}")
            return (seen[hb], i)
        seen[hb] = i
        board = nb

a,b = find_cycle(board) 

offset = (1000000000 - (a+1)) % (b - a)
print(f"(1000000000 - {(a+1)}) % {b - a} = {offset}")
index_to_check = a + offset
i = 0

while i <= index_to_check:
    board = cycle(board)
    i+=1

print(evaluate(board))

# 12c...nc...nc...n
#               x
