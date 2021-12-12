FILE = "day_eight.txt"
inputs = []
outputs = []

with open(FILE, "r") as f:
    lines = f.read().splitlines()
    for l in lines:
        inputs.append(l.split("|")[0].split())
        outputs.append(l.split("|")[1].split())
    
o = []
for t in outputs:
    for i in t:
        o.append(i)
        
part1 = 0
for x in o:
    if len(x) in {2, 4, 3, 7}:
        part1 += 1

print(part1)
sumSignals = 0

for i, inp in enumerate(inputs):
    NUMS = { x : "" for x in range(0, 10) }
    for s in inp:
        chars = [c for c in s]
        if len(s) == 2:
            NUMS[1] = set(chars)
        if len(s) == 3:
            NUMS[7] = set(chars)
        if len(s) == 4:
            NUMS[4] = set(chars)
        if len(s) == 7:
            NUMS[8] = set(chars)

    for s in inp:
        chars = [c for c in s]
        if len(s) == 5:
            if len(set(chars).intersection(NUMS[1])) == 2:
                NUMS[3] = set(chars)
            elif len(set(chars).intersection(NUMS[4])) == 3:
                NUMS[5] = set(chars)
            else:
                NUMS[2] = set(chars)
        
        if len(s) == 6:
            if len(set(chars).intersection(NUMS[4])) == 4:
                NUMS[9] = set(chars)
            elif len(set(chars).intersection(NUMS[7])) == 3:
                NUMS[0] = set(chars)
            else:
                NUMS[6] = set(chars)
    o = ""
    for op in outputs[i]:
        chars = [c for c in op]
        for n in NUMS:
            if NUMS[n] == set(chars):
                o += str(n)

    sumSignals += int(o)

print(sumSignals)