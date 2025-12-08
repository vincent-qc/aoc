from util import next_int, next_line, next_line_ints, next_word, read_whole

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def print_formatted_perim_grid(perim_grid):
    for row in perim_grid:
        print(['X' if x else ' ' for x in row])
    print()


def valid_position(grid, x, y):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])


def count_vertical(perim_grid, vertical_visited, x, y):
    if not valid_position(perim_grid, x, y):
        return 0
    if not perim_grid[x][y]:
        return 0
    if vertical_visited[x][y]:
        return 0
    vertical_visited[x][y] = True
    return 1 + count_vertical(perim_grid, vertical_visited, x, y + 1) + count_vertical(perim_grid, vertical_visited, x, y - 1)


def count_horizontal(perim_grid, horizontal_visited, x, y):
    if not valid_position(perim_grid, x, y):
        return 0
    if not perim_grid[x][y]:
        return 0
    if horizontal_visited[x][y]:
        return 0
    horizontal_visited[x][y] = True
    return 1 + count_horizontal(perim_grid, horizontal_visited, x, y + 1) + count_horizontal(perim_grid, horizontal_visited, x, y - 1)


def count_sides(perim_grid):
    xlen = len(perim_grid)
    ylen = len(perim_grid[0])
    horizontal_visited = [[False for i in range(ylen)] for j in range(xlen)]
    vertical_visited = [[False for i in range(ylen)] for j in range(xlen)]
    count = 0
    for i in range(xlen):
        for j in range(ylen):
            if perim_grid[i][j]:
                if not horizontal_visited[i][j]:
                    count = count_horizontal(
                        perim_grid, horizontal_visited, i, j)
                    if count > 1:
                        print("H:", i, j)
                        count += 1

                if not vertical_visited[i][j]:
                    count = count_vertical(
                        perim_grid, vertical_visited, i, j)
                    if count > 1:
                        print("V:", i, j)
                        count += 1
    print_formatted_perim_grid(horizontal_visited)

    return count


def valid_perim(perim_grid, x, y):
    perim_grid[x][y] = True
    for direction in directions:
        nx, ny = x + direction[0], y + direction[1]
        if not valid_position(perim_grid, nx, ny):
            continue
        if perim_grid[nx][ny]:
            return False
    return True


def find_area(grid, visited, perim_grid, x, y, char):
    if not valid_position(grid, x, y):
        perim_grid[x + 1][y + 1] = True
        return 0
    if grid[x][y] != char:
        perim_grid[x + 1][y + 1] = True
        return 0
    if visited[x][y]:
        return 0
    visited[x][y] = True
    area = 0
    for direction in directions:
        area += find_area(grid, visited, perim_grid, x +
                          direction[0], y + direction[1], char)
    return 1 + area


def main():
    grid = []
    for i in range(4):
        grid.append([char for char in next_line()])

    visited = [[False for i in range(4)] for j in range(4)]

    sum = 0
    for i in range(4):
        for j in range(4):
            if not visited[i][j]:
                perim_grid = [
                    [False for i in range(4 + 2)] for j in range(4 + 2)]
                area = find_area(
                    grid, visited, perim_grid, i, j, grid[i][j])
                sides = count_sides(perim_grid)
                print(grid[i][j], area, sides)
                print_formatted_perim_grid(perim_grid)
                sum += area * sides
                # print(perim_grid)
    print(sum)
    pass


main()
