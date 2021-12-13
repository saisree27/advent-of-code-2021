def horizontal_reflection(num, matrix):
    start = len(matrix) - 2 * num - 1
    end = len(matrix) - num - 1

    if num * 2 == len(matrix):
        start = len(matrix) - 2 * num + 1
        end = len(matrix) - num

    for y in range(start, end):
        for x in range(len(matrix[0])):
            if matrix[2 * num - y][x] == '#':
                matrix[y][x] = matrix[2 * num - y][x]
    
    matrix = matrix[:end]
    return matrix

def vertical_reflection(num, matrix):
    start = len(matrix[0]) - 2 * num - 1
    end = len(matrix[0]) - num - 1

    if num * 2 == len(matrix[0]):
        start = len(matrix[0]) - 2 * num + 1
        end = len(matrix[0]) - num

    for y in range(len(matrix)):
        for x in range(start, end):
            if matrix[y][2 * num - x] == '#':
                matrix[y][x] = matrix[y][2 * num - x]
    
    matrix = [row[:end] for row in matrix]
    return matrix

FILE = 'day_thirteen.txt'
lines = []

with open(FILE, 'r') as f:
    lines = f.read().splitlines()

max_width = 0
max_height = 0
points = []
done_points = False
horizontal_line = 0
vertical_line = 0
instructions = []

for line in lines:
    if line == "":
        done_points = True
    if not done_points:
        point = line.split(',')
        point = (int(point[0]), int(point[1]))
        max_width = max(max_width, point[1])
        max_height = max(max_height, point[0])
        points.append(point)
    else:
        if line != "":
            if 'x' in line:
                instructions.append((int(line.split('=')[-1]), 'V'))
            else:
                instructions.append((int(line.split('=')[-1]), 'H'))


matrix = [['.' for _ in range(max_height + 1)] for _ in range(max_width + 1)]

for x, y in points:
    matrix[y][x] = '#'

for index, i in enumerate(instructions):
    if i[1] == 'H':
        matrix = horizontal_reflection(i[0], matrix)
    else:
        matrix = vertical_reflection(i[0], matrix)

    if index == 0:
        count = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == '#':
                    count += 1
        print(count)

for row in matrix:
    print(*row)