from util import next_int, next_line, next_line_ints, next_word, read_whole

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def valid_pos(pos):
    return 0 <= pos[0] < 130 and 0 <= pos[1] < 130


def check_for_cycle(grid, start):
    visited = [[[False, False, False, False]
                for __ in range(130)] for _ in range(130)]
    guard_pos = start
    cur_dir = 0

    while valid_pos(guard_pos):
        next_pos = (guard_pos[0] + directions[cur_dir][0],
                    guard_pos[1] + directions[cur_dir][1])

        while valid_pos(next_pos) and grid[next_pos[0]][next_pos[1]] == '#':
            cur_dir = (cur_dir + 1) % 4
            next_pos = (guard_pos[0] + directions[cur_dir][0],
                        guard_pos[1] + directions[cur_dir][1])

            if visited[guard_pos[0]][guard_pos[1]][cur_dir]:
                return True
            else:
                visited[guard_pos[0]][guard_pos[1]][cur_dir] = True

        guard_pos = next_pos

    return False


def main():
    grid = [[__ for __ in range(130)] for _ in range(130)]

    guard_pos = (0, 0)
    for i in range(130):
        line = next_line()
        for j in range(130):
            grid[i][j] = line[j]
            if line[j] == "^":
                guard_pos = (i, j)

    count = 0

    for i in range(130):
        for j in range(130):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                if check_for_cycle(grid, guard_pos):
                    count += 1
                grid[i][j] = "."

    print(count)  # 1884


main()
