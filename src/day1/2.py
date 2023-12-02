lines = open("input.txt", "r").readlines()

def transform(line):
    spelled = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9}

    res = []
    for i in range(0, len(line)):
        for sp in spelled.keys():
            if line[i:].startswith(sp):
                res = res + [spelled[sp]]
        if line[i].isdigit():
            res = res + [int(line[i])]
    return res

#lines = ["two1nine" ,"eightwothree" ,"abcone2threexyz" ,"xtwone3four" ,"4nineeightseven2" ,"zoneight234" ,"7pqrstsixteen"]

s = 0
for line in lines:
    digits = transform(line)
    print(digits)
    d = int(str(digits[0]) + "" +  str(digits[-1]))
    s = s + d


print(s)

