from util import next_line

N = 6
M = 1000


def place(grid, cells, x, y):
    for (dx, dy) in cells:
        if grid[y+dy][x+dx] == '#':
            return False
    for (dx, dy) in cells:
        grid[y+dy][x+dx] = '#'
    return True


def remove(grid, cells, x, y):
    for (dx, dy) in cells:
        grid[y+dy][x+dx] = '.'


def bt(shapes, grid, queue, w, h):
    if not queue:
        return True

    cur = queue.pop()
    for (cells, sw, sh) in shapes[cur]:
        for y in range(h - sh + 1):
            for x in range(w - sw + 1):
                if place(grid, cells, x, y):
                    if bt(shapes, grid, queue, w, h):
                        return True
                    remove(grid, cells, x, y)
    queue.append(cur)
    return False


def start(shapes, grid):
    ((w, h), reqs) = grid

    queue = []
    area = 0
    for idx in range(len(reqs)):
        cnt = reqs[idx]
        queue.extend([idx] * cnt)
        if shapes[idx]:
            area += len(shapes[idx][0][0]) * cnt

    if area > w * h:
        return False

    queue.sort(key=lambda i: -len(shapes[i][0][0]))
    empty = [["."] * w for _ in range(h)]
    return bt(shapes, empty, queue, w, h)


def norm(cells):
    mx = min(c[0] for c in cells)
    my = min(c[1] for c in cells)
    return tuple(sorted((c[0]-mx, c[1]-my) for c in cells))


def permute(shape):
    def rot(s):
        return {(2-y, x) for (x, y) in s}

    def flip(s):
        return {(2-x, y) for (x, y) in s}

    cells = {(x, y) for y in range(3) for x in range(3) if shape[y][x] == '#'}

    seen = set()
    result = []
    cur = cells
    for _ in range(4):
        for s in [cur, flip(cur)]:
            n = norm(s)
            if n not in seen:
                seen.add(n)
                sw = max(c[0] for c in n) + 1
                sh = max(c[1] for c in n) + 1
                result.append((n, sw, sh))
        cur = rot(cur)

    return result


def solve():
    shapes = []
    for _ in range(N):
        _ = next_line()
        l1 = list(next_line())
        l2 = list(next_line())
        l3 = list(next_line())
        shapes.append(permute([l1, l2, l3]))
        _ = next_line()

    grids = []
    for _ in range(M):
        [dim, req] = next_line().split(": ")
        [x, y] = map(int, dim.split("x"))
        grids.append(((x, y), list(map(int, req.split(' ')))))

    res = 0
    for grid in grids:
        if start(shapes, grid):
            res += 1

    print(res)


solve()
