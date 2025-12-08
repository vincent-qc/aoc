import bisect

from util import next_int, next_line, next_line_ints, next_word, read_whole

L1 = 200

dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


ranges = []


def solve():
    for _ in range(L1):
        line = next_line()
        [s, e] = map(int, line.split("-"))
        ranges.append((s, e))

    ranges.sort()

    merged = [ranges[0]]
    for s, e in ranges[1:]:
        if s <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))

    count = 0
    for [s, e] in merged:
        count += (e-s + 1)
    print(count)


solve()
