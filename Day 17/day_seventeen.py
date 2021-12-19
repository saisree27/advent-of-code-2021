def simulate(pos, velocity):
    max_y = 0
    while pos[0] <= higher_x and pos[1] >= lower_y:
        pos[0] += velocity[0]
        pos[1] += velocity[1]

        max_y = max(max_y, pos[1])

        if lower_x <= pos[0] <= higher_x and lower_y <= pos[1] <= higher_y:
            return True, max_y

        if velocity[0] < 0:
            velocity[0] += 1
        elif velocity[0] > 0:
            velocity[0] -= 1
        
        velocity[1] -= 1
    return False, None

FILE = 'day_seventeen.txt'
area = open(FILE,'r').read().splitlines()[0][13:]
lower_x, higher_x = [int(x) for x in area.split(',')[0].split('=')[1].split('..')]
lower_y, higher_y = [int(x) for x in area.split(',')[1].split('=')[1].split('..')]

count = 0
max_height = 0
max_velocity = (0, 0)
for x in range(min(-abs(lower_y), -abs(higher_y)) - 1, max(abs(lower_x), abs(higher_x)) + 1):
    for y in range(min(-abs(lower_y), -abs(higher_y)) - 1, max(abs(lower_y), abs(higher_y)) + 1):
        res = simulate([0, 0], [x, y])
        if res[0]:
            count += 1
            if res[1] > max_height:
                max_height = res[1]
                max_velocity = (x, y)

print('Part 1: %s' % max_height)
print('Part 2: %s' % count)
