from util import next_int, next_line, next_word, read_whole


def is_safe(line_ints):
    def check_safety(ints):
        is_increasing = ints[0] < ints[1]
        for j in range(len(ints) - 1):
            if (is_increasing and ints[j] > ints[j + 1]) or (not is_increasing and ints[j] < ints[j + 1]):
                return False
            if abs(ints[j] - ints[j + 1]) > 3 or abs(ints[j] - ints[j + 1]) < 1:
                return False
        return True

    if check_safety(line_ints):
        return True

    for i in range(len(line_ints)):
        if check_safety(line_ints[:i] + line_ints[i+1:]):
            return True

    return False


def main():
    count = 0
    for i in range(1000):
        line = next_line()
        line_ints = [int(x) for x in line.split()]

        if is_safe(line_ints):
            count += 1

    print(f"Number of safe reports: {count}")


main()
