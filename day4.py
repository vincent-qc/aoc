from util import next_int, next_line, next_line_ints, next_word, read_whole

LINES = 136
W = LINES
H = LINES

dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def solve():
    grid = []
    for _ in range(LINES):
        row = list(next_line())
        grid.append(row)

    removing = True

    def ispaper(x, y):
        if x >= W or y >= H or x < 0 or y < 0:
            return False
        return grid[y][x] == '@'

    def check(x, y):
        paper = 0
        for (dx, dy) in dirs:
            nx = x + dx
            ny = y + dy
            if ispaper(nx, ny):
                paper += 1
        return paper < 4

    sum = 0
    while removing:
        removing = False
        for x in range(W):
            for y in range(H):
                if grid[y][x] == '@' and check(x, y):
                    sum += 1
                    grid[y][x] = '.'
                    removing = True

    print(sum)


solve()
