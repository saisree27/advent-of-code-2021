
list_sonars = []
with open("day_one.txt", "r") as f:
    for line in f.readlines():
        list_sonars.append(int(line))

print(len(list_sonars))

# part 1
count = 0
for i in range(1, len(list_sonars)):
    if list_sonars[i] > list_sonars[i - 1]:
        count += 1
    
print(count)

# part 2
count = 0
for i in range(1, len(list_sonars) - 2):
    window = list_sonars[i] + list_sonars[i + 1] + list_sonars[i + 2]
    prev_window = window - list_sonars[i + 2] + list_sonars[i - 1]
    print(prev_window)

    if window > prev_window:
        count += 1

print(count)