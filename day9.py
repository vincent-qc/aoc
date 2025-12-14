import bisect
import math

from util import file, next_int, next_line, next_line_ints, next_word, read_whole

N = 496


def area(a, b, x, y):
    return (abs((x-a))+1) * (abs((y-b))+1)


def solve():
    pairs = []
    for _ in range(N):
        [x, y] = list(map(int, next_line().split(',')))
        pairs.append((x, y))

    edges = []
    for i in range(N):
        edges.append((pairs[i], pairs[(i+1) % N]))

    xs = sorted(set(p[0] for p in pairs))
    ys = sorted(set(p[1] for p in pairs))

    W = len(xs)
    H = len(ys)

    def inside(px, py):
        crossings = 0
        for ((x1, y1), (x2, y2)) in edges:
            if x1 == x2 and px < x1:
                y_min, y_max = min(y1, y2), max(y1, y2)
                if y_min < py < y_max:
                    crossings += 1
        return crossings % 2 == 1

    cell_valid = [[False] * (H-1) for _ in range(W-1)]
    for i in range(W-1):
        for j in range(H-1):
            px = (xs[i] + xs[i+1]) / 2
            py = (ys[j] + ys[j+1]) / 2
            cell_valid[i][j] = inside(px, py)

    prefix = [[0] * H for _ in range(W)]
    for i in range(W-1):
        for j in range(H-1):
            val = 0 if cell_valid[i][j] else 1
            prefix[i+1][j+1] = val + prefix[i][j+1] + \
                prefix[i+1][j] - prefix[i][j]

    def query(i1, j1, i2, j2):
        return prefix[i2][j2] - prefix[i1][j2] - prefix[i2][j1] + prefix[i1][j1]

    x_to_i = {x: i for i, x in enumerate(xs)}
    y_to_j = {y: j for j, y in enumerate(ys)}

    largest = 0
    for i in range(N):
        for j in range(i+1, N):
            (a, b) = pairs[i]
            (x, y) = pairs[j]

            i1, i2 = sorted([x_to_i[a], x_to_i[x]])
            j1, j2 = sorted([y_to_j[b], y_to_j[y]])

            if query(i1, j1, i2, j2) == 0:
                largest = max(area(a, b, x, y), largest)

    print(largest)


solve()
