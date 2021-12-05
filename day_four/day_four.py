def win(b):
    found = False
    for row in range(0, 5):
        found = found or b[row][0] == b[row][1] == b[row][2] == b[row][3] == b[row][4] == '*'
    for col in range(0, 5):
        found = found or b[0][col] == b[1][col] == b[2][col] == b[3][col] == b[4][col] == '*'
    return found

def get_index(b, n):
    for x in range(0, 5):
        for y in range(0, 5):
            if b[x][y] == n:
                return (x, y)
    return -99

FILE = "input.txt"
list_boards = []
nums = []

with open(FILE, "r") as f:
    board = []
    for i, line in enumerate(f.read().splitlines()):
        if i == 0:
            nums = line.split(",")
        elif line == "":
            if i > 1:
                list_boards.append(board)
                board = []
        else:
            board.append(line.split())

to_remove = []
for num in nums:
    for i, board in enumerate(list_boards):
        index = get_index(board, num)
        if index != -99:
            board[index[0]][index[1]] = '*'
            if win(board):
                to_remove.append(i)
                unmarked = []
                for r in range(0, 5):
                    for c in range(0, 5):
                        if board[r][c] != '*':
                            unmarked.append(int(board[r][c]))
                print(str(int(num) * sum(unmarked)) + " (" + str(int(num)) + " x " + str(sum(unmarked)) + ")")

    for x in to_remove:
        list_boards = list_boards[:x] + list_boards[x + 1:]

    to_remove = []
    
    print("%s boards left." % len(list_boards))

