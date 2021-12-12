def process_line(line):
    opening = set(['[', '{', '<', '('])
    closing = set([']', '}', '>', ')'])
    o_to_c = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>'
    }
    
    stack = []

    for c in line:
        if c in opening:
            stack.append(c)
        if c in closing:
            if o_to_c[stack[-1]] == c:
                stack.pop()
            else:
                return c
    
    if len(stack) == 0:
        return True
    else:
        remaining = []
        while len(stack) != 0:
            remaining.append(o_to_c[stack.pop()])
        return remaining


FILE = "day_ten.txt"
lines = []

with open(FILE, 'r') as f:
    lines = f.read().splitlines()

errors = []
incompletes = []
for l in lines:
    res = process_line(l)
    if res == True:
        pass
    elif res[0] == res:
        errors.append(res)
    else:
        incompletes.append(res)

lookup = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

lookup_two = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

sum_errors = sum([lookup[x] for x in errors])
print(sum_errors)

sum_incompletes = []
for x in incompletes:
    sum_i = 0
    for y in x:
        sum_i *= 5
        sum_i += lookup_two[y]
    sum_incompletes.append(sum_i)

sum_incompletes = list(sorted(sum_incompletes))
print(sum_incompletes[len(sum_incompletes) // 2])

