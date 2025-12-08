import bisect

from util import file, next_int, next_line, next_line_ints, next_word, read_whole

N = 4


def solve():
    matrix = []
    for i in range(N):
        line = file.readline().rstrip('\n')
        matrix.append(list(line))

    line = next_line()
    ops = []
    for c in reversed(line):
        if c != " ":
            ops.append(c)

    def iscol(x):
        for y in range(N):
            c = matrix[y][x]
            if c != ' ':
                return True
        return False

    def colnum(x):
        res = ""
        for y in range(N):
            c = matrix[y][x]
            if c == ' ':
                continue
            res += c
        return int(res)

    # Process right to left
    ops_i = 0
    x = len(matrix[0]) - 1
    nums = []
    while x >= 0:
        op = ops[ops_i]
        result = 0 if op == '+' else 1
        while x >= 0 and iscol(x):
            if op == '+':
                result += colnum(x)
            else:
                result *= colnum(x)
            x -= 1
        nums.append(result)
        ops_i += 1
        x -= 1
    print(sum(nums))


solve()
