def do_flash(x, y, matrix, flashed):
    flashed.add((x, y))
    if x > 0:
        matrix[x - 1][y] += 1
        if matrix[x - 1][y] > 9 and (x - 1, y) not in flashed:
            do_flash(x - 1, y, matrix, flashed)
    if x > 0 and y > 0:
        matrix[x - 1][y - 1] += 1
        if matrix[x - 1][y - 1] > 9 and (x - 1, y - 1) not in flashed:
            do_flash(x - 1, y - 1, matrix, flashed)        
    if y > 0:
        matrix[x][y - 1] += 1
        if matrix[x][y - 1] > 9 and (x, y - 1) not in flashed:
            do_flash(x, y - 1, matrix, flashed)
    if y > 0 and x < len(matrix) - 1:
        matrix[x + 1][y - 1] += 1
        if matrix[x + 1][y - 1] > 9 and (x + 1, y - 1) not in flashed:
            do_flash(x + 1, y - 1, matrix, flashed)
    if x < len(matrix) - 1:
        matrix[x + 1][y] += 1
        if matrix[x + 1][y] > 9 and (x + 1, y) not in flashed:
            do_flash(x + 1, y, matrix, flashed)
    if x < len(matrix) - 1 and y < len(matrix[0]) - 1:
        matrix[x + 1][y + 1] += 1
        if matrix[x + 1][y + 1] > 9 and (x + 1, y + 1) not in flashed:
            do_flash(x + 1, y + 1, matrix, flashed)
    if y < len(matrix[0]) - 1:
        matrix[x][y + 1] += 1
        if matrix[x][y + 1] > 9 and (x, y + 1) not in flashed:
            do_flash(x, y + 1, matrix, flashed)
    if y < len(matrix[0]) - 1 and x > 0:
        matrix[x - 1][y + 1] += 1
        if matrix[x - 1][y + 1] > 9 and (x - 1, y + 1) not in flashed:
            do_flash(x - 1, y + 1, matrix, flashed)
    return

def execute_step(matrix):
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[0])):
            matrix[r][c] += 1
    
    flashed = set()
    for r in range(0, len(matrix)):
        for c in range(0, len(matrix[0])):
            if matrix[r][c] > 9:
                do_flash(r, c, matrix, flashed)
                for x, y in flashed:
                    matrix[x][y] = 0
    
    if len(flashed) == 100:
        return len(flashed), True
    else:
        return len(flashed), False

FILE = "day_eleven.txt"
lines = []

with open(FILE, 'r') as f:
    lines = f.read().splitlines()

octopuses = []

for l in lines:
    octopuses.append([int(c) for c in l])

num_flashes = 0
got_first = False
for step in range(1000):
    num, all_flashed = execute_step(octopuses)
    if step < 100:
        num_flashes += num
    if all_flashed and not got_first:
        print(step + 1)
        got_first = True

print(num_flashes)

