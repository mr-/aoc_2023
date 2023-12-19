import sys
from heapdict import heapdict
from collections import defaultdict


def parse(lines):
    board = {}
    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
                c = lines[y][x]
                board[(x,y)] = int(c)
    return board

#it can move at most three blocks in a single direction before it must turn 90 degrees left or right. 
#The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.


def get_neighbors(graph, n):
    dirs = [
        (+ 0, + 1),
        (+ 0, - 1),
        (+ 1, + 0),
        (- 1, + 0)]
    # can't go back
    if n[1] != (0,0):
        dirs.remove((-n[1][0], -n[1][1]))

    for d in dirs:
        np = (n[0][0] + d[0], n[0][1]+ d[1])
        if not np in graph:
            continue
        if d != n[1]:
            # changed direction
            yield (np, d, 0)
        else:
            # same direction
            new_count = n[2] + 1
            # too much?
            if new_count < 3:
                yield(np, d, new_count) 

    
def dijkstra(graph, start_node):
    shortest_path = defaultdict(lambda: sys.maxsize)
    # need to keep track of the direction and number of steps in that direction 
    shortest_path[(start_node, (0,0), 0)] = 0

    queue = heapdict()
    queue[(start_node, (0,0), 0)] = 0
    prev = {}
    
    while queue:
        n, current_dist = queue.popitem()
                
        for neighbor in get_neighbors(graph, n):
            d = current_dist + graph[neighbor[0]]
            if d < shortest_path[neighbor]:
                queue[neighbor] = d
                shortest_path[neighbor] = d
                prev[neighbor] = n
            if d == shortest_path[neighbor]:
                queue[neighbor] = d
    
    return (shortest_path, prev)



def to_list(res, pos):
    while pos[0] != (0,0):
        yield pos[0]
        pos = res[pos]

graph = parse([l.strip() for l in open("sample.txt").readlines()])
graph = parse([l.strip() for l in open("input.txt").readlines()])

res, prev = dijkstra(graph, (0,0))




def pp(prev, end):
    maxx = max([x[0][0] for x in prev.values()])
    maxy = max([x[0][1] for x in prev.values()])
    path = {p:i for i, p in enumerate(to_list(prev, end))}
    i = 0
    for y in range(0, maxy+1):
        for x in range(0, maxx+1):
            if (x,y) in path:
                print(f"{path[(x,y)] % 10}" , end="")
                i += 1
            else:
                print(".", end="")
        print()


maxx = max([x[0][0] for x in prev.values()])
maxy = max([x[0][1] for x in prev.values()])
x = min([(res[k], k) for k in res.keys() if k[0] == (maxx,maxy)], key=lambda x: x[0])

pp(prev, x[1])
print(x)
#print(res[1][(11,12)])
