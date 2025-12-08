from util import next_int, next_line, next_line_ints, next_word, read_whole

LINES = 200


def tmp(line):
    result = 0
    p = -1
    for n in range(11, -1, -1):
        m = 0
        best_i = p
        a = None if n == 0 else -n
        for i, c in enumerate(line[p+1:a]):
            d = int(c)
            if d > m:
                best_i = p + 1 + i
                m = d
        p = best_i
        result = result * 10 + m
    return result


def solve():
    sum = 0
    for _ in range(LINES):
        line = next_line()
        num = tmp(line)

        sum += num

    print(sum)


solve()
