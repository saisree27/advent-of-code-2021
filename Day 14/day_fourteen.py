from collections import defaultdict

def process_polymer(p, rules):
    new_p = ''
    for i in range(len(p) - 1):
        pair = p[i:i + 2]
        if pair in rules:
            new_p += pair[0] + rules[pair]
    new_p += pair[1]
    return new_p

def process_polymer_two(p, rules):
    for pair, c in list(p.items()):
        if pair in rules and c > 0:
            a = pair[0] + rules[pair]
            b = rules[pair] + pair[1]
            p[pair] -= c
            p[a] += c
            p[b] += c
    
    return p

def convert_to_map(q):
    map_polymer = defaultdict(lambda: 0)
    for i in range(len(q) - 1):
        map_polymer[q[i:i + 2]] += 1
    return map_polymer

FILE = 'day_fourteen.txt'
lines = []
polymer = ''
rules = {}

with open(FILE, 'r') as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    if i == 0:
        polymer = line
    elif line == '':
        pass
    else:
        rule = line.split(' -> ')
        rules[rule[0]] = rule[1]


polymerMap = convert_to_map(polymer)

for i in range(40):
    # part 1
    # polymer = process_polymer(polymer, rules)
    polymerMap = process_polymer_two(polymerMap, rules)

map_freq = {}
for pair in polymerMap:
    if polymerMap[pair] > 0:
        _, y = pair
        if y in map_freq:
            map_freq[y] += polymerMap[pair]
        else:
            map_freq[y] = polymerMap[pair]

largest = 0
smallest = float("inf")

for x in map_freq:
    largest = max(largest, map_freq[x])
    smallest = min(smallest, map_freq[x])

print(largest - smallest)