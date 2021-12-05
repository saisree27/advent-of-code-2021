FILE = "day_five.txt"
points = []
max_point = 0

with open(FILE, "r") as f:
    for i, line in enumerate(f.read().splitlines()):
        d = line.split(" ")
        x1 = int(d[0].split(",")[0])
        y1 = int(d[0].split(",")[1])
        x2 = int(d[2].split(",")[0])
        y2 = int(d[2].split(",")[1])
        max_point = max(max_point, x1, y1, x2, y2)

        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, i))
        elif y1 == y2:
            for i in range(min(x1, x2), max(x1, x2)  + 1):
                points.append((i, y1))
        else:
            # part 2 (diagonal lines)
            # uncomment for part 1
            slope = (y2 - y1) / (x2 - x1)
            if abs(slope) == 1.0:
                x = x1 if min(y1, y2) == y1 else x2
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    points.append((x, i))
                    x += int(slope)


grid = [[0 for _ in range(max_point + 1)] for _ in range(max_point + 1)]

for x, y in points:
    grid[x][y] += 1

ans = 0
for r in range(max_point + 1):
    for c in range(max_point + 1):
        if grid[r][c] >= 2:
            ans += 1

print(ans)