import networkx as nx
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
directions = {
    "|": {"N", "S"},
    "-": {"W", "E"},
    "L": {"N", "E"},
    "J": {"N", "W"},
    "7": {"S", "W"},
    "F": {"S", "E"},
    ".": {},
    "S": {},
}

def parse(lines):
    res = {}
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            c = lines[y][x]
            if c == '\n':
                continue
            res[(x,y)] = directions[c]
            if c == "S":
                res["start"] = (x,y)
    return res


def start_with(grid, pipe):
    grid[grid["start"]] = pipe
    return grid


def make_graph(grid):
    G = nx.Graph()
    for k in grid.keys():
        if k == "start":
            continue
        for d in [((1,0), ("E", "W")), ((0,1), ("S", "N")), ((-1, 0), ("W", "E")), ((0, -1), ("N", "S"))]:
            kn = (k[0] + d[0][0], k[1] + d[0][1])
            G.add_node(k)
            G.add_node(kn)
            pk = grid.get(k, {})
            pkn = grid.get(kn, {})
            if d[1][0] in pk and d[1][1] in pkn:
                if not G.has_edge(k, kn):
                    G.add_edge(k, kn)
    return G



lines = open("sample1.txt").readlines()
lines = open("input.txt").readlines()
grid = parse(lines)

for start in [{"N", "S"}, {"W", "E"}, {"N", "E"}, {"N", "W"}, {"S", "W"}, {"S", "E"}]:
    grid = start_with(grid, start)
    G = make_graph(grid)

    try:
        cycles = nx.find_cycle(G, source=grid["start"]) 
        print(len(cycles)/2)
    except:
        print(f"no cycle for {start}")


