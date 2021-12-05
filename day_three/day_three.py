DIGITS = 12
FILE = "input.txt"

list_counters = [[0, 0] for _ in range(0, DIGITS)]

with open(FILE, "r") as f:
    for line in f.readlines():
        i = 0
        for digit in line:
            if digit != "\n":
                list_counters[i][int(digit)] += 1 
            i += 1

gamma = ""
for zero, one in list_counters:
    if one > zero:
        gamma += "1"
    else:
        gamma += "0"

epsilon = ""
for zero, one in list_counters:
    if one < zero:
        epsilon += "1"
    else:
        epsilon += "0"

print("PART ONE: " + str(int(gamma, 2) * int(epsilon, 2)))

nums = []

with open(FILE, "r") as f:
    for line in f.readlines():
        nums.append(line.replace("\n", ""))

# oxygen generator
o_gen = ""
digits = {
    "0": [],
    "1": []
}

temp = nums
for digit in range(DIGITS):
    for n in temp:
        if n[digit] == "0":
            digits["0"].append(n)
        else:
            digits["1"].append(n)
    if len(digits["0"]) > len(digits["1"]):
        temp = digits["0"]
    else:
        temp = digits["1"]
    
        
    digits = {
        "0": [],
        "1": []
    }

    if len(temp) == 1:
        o_gen = temp[0]
        break

# co2 generator
c_gen = ""
digits = {
    "0": [],
    "1": []
}
temp = nums

for digit in range(12):
    for n in temp:
        if n[digit] == "0":
            digits["0"].append(n)
        else:
            digits["1"].append(n)

    if len(digits["0"]) <= len(digits["1"]):
        temp = digits["0"]
    else:
        temp = digits["1"]

    digits = {
        "0": [],
        "1": []
    } 

    if len(temp) == 1:
        c_gen = temp[0]

print("PART TWO " + str(int(o_gen, 2) * int(c_gen, 2)))