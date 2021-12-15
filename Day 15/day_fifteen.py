from collections import defaultdict
import heapq
import numpy as np

def dijkstras(adj_list, start, matrix):
    visited = set()
    distances = {}
    pq = []

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            distances[(r, c)] = float("inf")
    
    heapq.heappush(pq, (0, start))

    while len(pq) != 0 and len(visited) != len(matrix) * len(matrix[0]):
        dist, vertex = heapq.heappop(pq)
        if vertex not in visited:
            visited.add(vertex)
            distances[vertex] = dist
            for vert, d in adj_list[vertex]:
                if vert not in visited:
                    heapq.heappush(pq, (d + dist, vert))
    
    return distances

FILE = 'day_fifteen.txt'
matrix = []


with open(FILE, 'r') as f:
    lines = f.read().splitlines()
    for l in lines:
        matrix.append([int(x) for x in l])

# part 2
matrix = np.array(matrix)
matrix = np.block([[(matrix + i + j - 1) % 9 + 1 for i in range(5)] for j in range(5)])

adj = defaultdict(lambda: [])
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if r > 0:
            adj[(r, c)].append( ((r - 1, c), matrix[r - 1][c]) )
        if c > 0:
            adj[(r, c)].append( ((r, c - 1), matrix[r][c - 1]) )
        if r < len(matrix) - 1:
            adj[(r, c)].append( ((r + 1, c), matrix[r + 1][c]) )
        if c < len(matrix[0]) - 1:
            adj[(r, c)].append( ((r, c + 1), matrix[r][c + 1]) )

distances = dijkstras(adj, (0, 0), matrix)
print(distances[(len(matrix) - 1, len(matrix[0]) - 1)])