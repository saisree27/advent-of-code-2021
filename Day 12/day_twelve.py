def count_paths(u, v, graph, visited, count):
    if not u.isupper():
        visited.add(u)
    if u == v:
        count[0] += 1
    else:
        for edge in graph[u]:
            if edge not in visited:
                count_paths(edge, v, graph, visited, count)
    
    if not u.isupper():
        visited.remove(u)

def count_paths_rep(u, v, graph, visited, count, a, c):
    if not u.isupper() and u != a:
        visited.add(u)
    if u == a and c >= 2:
        visited.add(a)
    if u == v:
        count[0] += 1
    
    else:
        for edge in graph[u]:
            if edge not in visited:
                if edge == a:
                    count_paths_rep(edge, v, graph, visited, count, a, c + 1)
                else:
                    count_paths_rep(edge, v, graph, visited, count, a, c)
    
    if not u.isupper() and u != a:
        visited.remove(u)
    if u == a and c >= 2:
        visited.remove(a)


FILE = "day_twelve.txt"
adj_list = {}
lines = []

with open(FILE, 'r') as f:
    lines = f.read().splitlines()

for l in lines:
    u, v = l.split("-")
    if u in adj_list:
        adj_list[u].append(v)
    else:
        adj_list[u] = [v]
    if v in adj_list:
        adj_list[v].append(u)
    else:
        adj_list[v] = [u]

num_paths = [0]
count_paths('start', 'end', adj_list, set(), num_paths)
print("Part 1: %s" % num_paths[0])

num_double_paths = 0
for x in adj_list:
    np = [0]
    if x.islower() and x != 'start' and x != 'end':
        count_paths_rep('start', 'end', adj_list, set(), np, x, 0)
        num_double_paths += np[0] - num_paths[0]

num_double_paths += num_paths[0]
print("Part 2: %s" % num_double_paths)
