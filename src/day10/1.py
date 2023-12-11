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
    res_points = set()
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            c = lines[y][x]
            if c == '\n':
                continue
            res[(x,y)] = directions[c]
            if c == "S":
                res["start"] = (x,y)
            if c == '.':
                res_points.add((x,y))
    return (res, res_points)


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
lines = open("sample2.2.txt").readlines()
lines = open("sample2.3.txt").readlines()
lines = open("input.txt").readlines()
grid, points = parse(lines)

def find_cycle(grid):
  for start in [{"N", "S"}, {"W", "E"}, {"N", "E"}, {"N", "W"}, {"S", "W"}, {"S", "E"}]:
      grid = start_with(grid, start)
      G = make_graph(grid)
  
      try:
          cycles = nx.find_cycle(G, source=grid["start"]) 
          return [p[0] for p in cycles]
      except:
          pass

def intersects(cycle, p):
    i= cycle.index(p)
    l = len(cycle)
    b = cycle[(i-1) % l]
    a = cycle[(i+1) % l]

    # we want to rule out "touch points", i.e. hitting p in 
    # a.
    # pb
    if {(0,0), (b[0] - p[0], b[1]-p[1]), (a[0] - p[0], a[1]-p[1])} == {(0,0), (0, -1), (1,0)}:
        return False
    # and 
    # ap
    # .b
    if {(0,0), (b[0] - p[0], b[1]-p[1]), (a[0] - p[0], a[1]-p[1])} == {(0,0), (0, 1), (-1,0)}:
        return False
    return True

def is_inside(cycle, p):
    line = [(p[0] - d, p[1] - d) for d in range(0, min(p)+1)]
    potential_intersections = set(line) & set(cycle)
    intersections = [q for q in potential_intersections if intersects(cycle, q)]

    if len(intersections)%2 != 0:
        return True
    else:
        return False


cycle = find_cycle(grid)
#print(cycle)
#print(is_inside(cycle, (9,8)))

points = grid.keys() - set(cycle) - {"start"}
inner = [p for p in points if is_inside(cycle, p)]
# print(points)
# print(inner)
print(len(inner))
