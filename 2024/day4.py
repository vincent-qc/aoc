from util import next_int, next_line, next_line_ints, next_word, read_whole

grid = []

directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
str = "MAS"


def search(i, j, direction, index):
    if index == 3:
        return 1
    if i < 0 or i >= 140 or j < 0 or j >= 140:
        return 0

    if grid[i][j] != str[index]:
        return 0
    return search(i + directions[direction][0], j + directions[direction][1], direction, index + 1)


def main():
    for _ in range(140):
        grid.append([c for c in next_line()])

    sum = 0

    for i in range(140):
        for j in range(140):
            if grid[i][j] == 'A':
                is_x = 0
                for direction in range(4):
                    is_x += search(
                        i - directions[direction][0], j - directions[direction][1], direction, 0)

                if is_x == 2:
                    sum += 1

    print(sum)


main()
