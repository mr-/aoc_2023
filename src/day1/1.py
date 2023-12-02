lines = open("input.txt", "r").readlines()
s = 0

for line in lines:
    digits = [c for c in line if c.isdigit()]
    d = int(digits[0] + "" + digits[-1])
    s = s + d

print(s)


