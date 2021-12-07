memo = {}
def calc_fuel(n):
    if n in memo:
        return memo[n]
    f = 0
    c = 1
    for i in range(n):
        f += c
        c += 1
    memo[n] = f
    return f

FILE = "day_seven.txt"
crabs = []

with open(FILE, "r") as f:
    crabs = f.read().splitlines()[0].split(",")
    crabs = [int(c) for c in crabs]

min_fuel = float("inf")
min_i = -99
for i in range(max(crabs)):
    fuel = 0
    for c in crabs:
        # part 1
        # fuel += abs(c - i)
        # part 2
        fuel += calc_fuel(abs(c - i))
    if fuel < min_fuel:
        min_fuel = fuel
        min_i = i

print(min_fuel)