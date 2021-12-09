def calculate_basin(x, y, matrix, visited):
    if (x, y) in visited:
        return 0
    if not (x >= 0 and y >= 0 and x < len(matrix) and y < len(matrix[0])):
        return 0
    if matrix[x][y] == 9:
        return 0

    visited.add((x, y))

    return 1 + calculate_basin(x + 1, y, matrix, visited) + calculate_basin(x, y + 1, matrix, visited) \
             + calculate_basin(x - 1, y, matrix, visited) + calculate_basin(x, y - 1, matrix, visited)
    


FILE = "day_nine.txt"
matrix = []

with open(FILE, "r") as f:
    lines = f.read().splitlines()
    for l in lines:
        matrix.append([int(s) for s in l])

sum_risks = 0
basin_sizes = []

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        check = True
        if x != 0:
            check = check and matrix[x][y] < matrix[x - 1][y]
        if y != 0:
            check = check and matrix[x][y] < matrix[x][y - 1]
        if x != len(matrix) - 1:
            check = check and matrix[x][y] < matrix[x + 1][y]
        if y != len(matrix[0]) - 1:
            check = check and matrix[x][y] < matrix[x][y + 1]
        
        if check:
            sum_risks += matrix[x][y] + 1
            basin_sizes.append(calculate_basin(x, y, matrix, set()))

print(sum_risks)
basin_sizes = sorted(basin_sizes)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])