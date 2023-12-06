from functools import reduce
from math import sqrt, ceil, floor
# Time:        48     98     90     83
# Distance:   390   1103   1112   1360

input = [{"time": 48989083, "distance": 390110311121360}]

# Time:      7  15   30
# Distance:  9  40  200

#input = [{"time": 71530, "distance": 940200}]


#input = [{"time": 48, "distance": 390}, {"time": 98, "distance": 1103},{"time": 90, "distance": 1112},{"time": 83, "distance": 1360}]

# Time:      7  15   30
# Distance:  9  40  200

#input = [{"time": 7, "distance": 9}, {"time": 15, "distance": 40},{"time": 30, "distance": 200}]


# given some time total, press for time t, have speed t, reach distance 
# (T-t)*t

# (T-t)*t = D
# t**2 - T*t + D = 0
# two solutions
# (T + sqrt(T**2 - 4D))/2
# (T - sqrt(T**2 - 4D))/2

def wins2(race):
    total = race["time"]
    d = race["distance"]
    x1 = (total + sqrt(total * total - 4 * d))/2
    x2 = (total - sqrt(total * total - 4 * d))/2
    return ceil(x1) - floor(x2) - 1



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
#    print([wins(race) for race in input])
    print([wins2(race) for race in input])



solve(input)
