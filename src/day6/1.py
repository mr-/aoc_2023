from functools import reduce
# Time:        48     98     90     83
# Distance:   390   1103   1112   1360

input = [{"time": 48, "distance": 390}, {"time": 98, "distance": 1103},{"time": 90, "distance": 1112},{"time": 83, "distance": 1360}]

# Time:      7  15   30
# Distance:  9  40  200

#input = [{"time": 7, "distance": 9}, {"time": 15, "distance": 40},{"time": 30, "distance": 200}]


# given some time total, press for time t, have speed t, reach distance 
# (T-t)*t

def dist(total, t):
    return (total - t)*t

def wins(race):
    s = 0
    for t in range(race["time"]):
        travelled = dist(race["time"], t)
        if travelled > race["distance"]:
            s += 1
    return s

def prd(l):
    return reduce(lambda x, y: x * y, l)

def solve(input):
    return prd([wins(race) for race in input])



print(solve(input))
