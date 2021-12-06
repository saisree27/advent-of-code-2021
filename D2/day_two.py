map_dirs = {
    "forward": 0,
    "down": 0,
    "up": 0
}
with open("day_two.txt", "r") as f:
    for line in f.readlines():
        direction = line.split(" ")[0]
        val = int(line.split(" ")[1])

        map_dirs[direction] += val

horizontal = map_dirs["forward"]
vertical = map_dirs["down"] - map_dirs["up"]

print(horizontal)
print(vertical)
print(horizontal * vertical)

print("PART TWO")
# part 2
aim = 0
horizontal = 0
vertical = 0

with open("day_two.txt", "r") as f:
    for line in f.readlines():
        direction = line.split(" ")[0]
        val = int(line.split(" ")[1])

        if direction == "up":
            aim -= val
        if direction == "down":
            aim += val
        if direction == "forward":
            horizontal += val
            vertical += val * aim

print(horizontal)
print(vertical)
print(horizontal * vertical)