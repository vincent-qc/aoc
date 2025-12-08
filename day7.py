import bisect

from util import file, next_int, next_line, next_line_ints, next_word, read_whole

N = 142


def solve():
    grid = [list(next_line()) for _ in range(N)]

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                S = (x, y)

    dp = [[-1] * len(grid[0]) for _ in range(N)]

    def dfs(cur):
        (x, y) = cur
        if y == N:
            return 1

        if dp[y][x] != -1:
            return dp[y][x]

        if grid[y][x] == '^':
            count = dfs((x-1, y+1)) + dfs((x+1, y+1))
        else:
            count = dfs((x, y+1))
        dp[y][x] = count
        return count

    print(dfs(S))


solve()
