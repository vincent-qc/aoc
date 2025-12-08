from util import next_int, next_line, next_line_ints, next_word, read_whole


def solve():
    pos = 50
    count = 0
    for _ in range(4068):
        l = next_line()
        dir = l[0]
        num = int(l[1:])

        if dir == 'R':
            count += (pos + num) // 100 - pos // 100
            pos = (pos + num) % 100
        elif dir == 'L':
            count += ((pos - 1) // 100) - (pos - num - 1) // 100
            pos = (pos - num) % 100
    print(count)


solve()
