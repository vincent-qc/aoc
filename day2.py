from util import next_int, next_line, next_line_ints, next_word, read_whole


def check(num):
    s = str(num)
    l = len(s)
    for i in range(1, l):
        if l % i != 0:
            continue

        same = True
        first = s[:i]
        for j in range(i, l, i):
            b = s[j:j+i]
            if b != first:
                same = False
                break

        if same:
            return True


def solve():
    l = next_line()
    ranges = list(
        map(lambda x: [int(x.split("-")[0]), int(x.split("-")[1])], l.split(",")))

    sum = 0
    for [s, e] in ranges:
        for num in range(s, e+1):
            iv = check(num)
            if iv:
                sum += num
    print(sum)


solve()
