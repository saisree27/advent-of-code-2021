import math

def convertHex(a):
    return str(hex(a))[2:].upper()

def convertBin(a):
    return '0' * (4 - len(str(bin(a))[2:])) + str(bin(a))[2:]

operations = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    4: lambda args: args[0],
    5: lambda args: 1 if args[0] > args[1] else 0,
    6: lambda args: 1 if args[0] < args[1] else 0,
    7: lambda args: 1 if args[0] == args[1] else 0
}


def processPacket(s, start):
    index = start
    version = s[index:index + 3]
    versions.append(int(version, 2))
    packet_ID = int(s[index + 3:index + 6], 2)
    index += 6

    if packet_ID == 4:
        values = []

        group = s[index]
        value = ''
        while group == '1':
            value += s[index + 1: index + 5]
            group, index = s[index + 5], index + 5

        value += s[index + 1: index + 5]
        values.append(int(value, 2))
        index += 5
    else:
        values = []
        length_ID = s[index]

        if length_ID == '0':
            end = index + 16 + int(s[index + 1: index + 16], 2)
            index += 16
            while index < end:
                index, value = processPacket(s, index)
                values.append(value)
        else:
            end = int(s[index + 1: index + 12], 2)
            index += 12
            for _ in range(end):
                index, value = processPacket(s, index)
                values.append(value)

    values = [v if type(v) == type(1) else v[0] for v in values]
    return index, operations[packet_ID](values)

versions = []

FILE = 'day_sixteen.txt'
hexadecimal = open(FILE, 'r').read().splitlines()[0]
hex_to_bin = {convertHex(x) : convertBin(x) for x in range(16)}
bin_str = ''

for c in hexadecimal:
    bin_str += hex_to_bin[c]

print('Part 2: %s' % processPacket(bin_str, 0)[1])

print('Part 1: %s' % sum(versions))