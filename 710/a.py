import sys


def main():
    moves = 0
    input = sys.stdin.readline()
    column = str(input[0])
    row = int(input[1])

    if column == 'a' or column == 'h':
        if row == 1 or row == 8:
            moves = 3
        elif row > 1 and row < 8:
            moves = 5
    elif column > 'a' and column < 'h':
        if row == 1 or row == 8:
            moves = 5
        elif row > 1 and row < 8:
            moves = 8

    print(moves)
main()

