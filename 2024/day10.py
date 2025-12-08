from util import next_int, next_line, next_line_ints, next_word, read_whole

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def valid_pos(x, y):
    return x >= 0 and x < 47 and y >= 0 and y < 47


def dfs(grid, visited, x, y, height):
    if not valid_pos(x, y):
        return 0

    if height != grid[x][y]:
        return 0
    # print("H:", height)
    if height == 9:
        # if visited[x][y]:
        #     return 0
        # visited[x][y] = True
        return 1

    sum = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        sum += dfs(grid, visited, nx, ny, height + 1)
    return sum


def main():
    grid = [[__ for __ in range(47)] for _ in range(47)]
    for i in range(47):
        line = next_line()
        for j in range(47):
            grid[i][j] = int(line[j])

    sum = 0
    for i in range(47):
        for j in range(47):
            if grid[i][j] == 0:
                visited = [[False for __ in range(47)] for _ in range(47)]
                res = dfs(grid, visited, i, j, 0)
                print(i, j)
                print(res)
                sum += res
    print(sum)


main()
