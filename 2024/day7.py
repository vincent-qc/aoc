from util import next_int, next_line, next_line_ints, next_word, read_whole


def try_possible(sum, rest, index, cur):
    if cur > sum:
        return False
    if index == len(rest):
        return cur == sum

    concatenated = int(str(cur) + str(rest[index]))
    return (
        try_possible(sum, rest, index + 1, cur + rest[index]) or
        try_possible(sum, rest, index + 1, cur * rest[index]) or
        try_possible(sum, rest, index + 1, concatenated)
    )


def main():

    sum = 0
    for i in range(850):
        line = next_line()
        split = line.split(" ")
        first = int(split[0][:len(split[0])-1])
        rest = [int(j) for j in split[1:]]

        if try_possible(first, rest, 0, 0):
            sum += first

    print(sum)

    pass


main()
