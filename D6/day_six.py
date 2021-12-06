FILE = "day_six.txt"
NUM_DAYS = 256
fish = []

with open(FILE, "r") as f:
    line = f.read().splitlines()[0]
    fish = [int(x) for x in line.split(",")]

def sum_fish(day, f, memo):
    if day == NUM_DAYS:
        return 1
    if (day, f) in memo:
        return memo[(day, f)]

    if f != 0:
        memo[(day, f)] = sum_fish(day + 1, f - 1, memo)
        return memo[(day, f)]
    
    memo[(day, f)] = sum_fish(day + 1, 8, memo) + sum_fish(day + 1, 6, memo)
    return memo[(day, f)]


print(sum([sum_fish(0, f, {}) for f in fish]))
