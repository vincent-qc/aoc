from util import next_int, next_line, next_line_ints, next_word, read_whole


def get_blankspaces(arr, index):
    count = 0
    for i in range(index, len(arr)):
        if arr[i] != -1:
            return count
        count += 1
    return count


def get_reverse_block(arr, index, char):
    count = 0
    for i in range(index, -1, -1):
        if arr[i] != char:
            return count
        count += 1
    return count


def find_first_opening(arr, length):
    index = 0
    while index < len(arr):
        if get_blankspaces(arr, index) >= length:
            return index
        index += 1
    return -1


def main():
    line = next_line()
    arr = []
    for i in range(len(line)):
        if i % 2 == 0:
            for j in range(int(line[i])):
                arr.append(int(i / 2))
        else:
            for j in range(int(line[i])):
                arr.append(-1)

    print(arr)

    p2 = len(arr) - 1
    while p2 > 0:
        print("P2:", p2)
        if arr[p2] == -1:
            p2 -= 1
            continue

        reverse_block = get_reverse_block(arr, p2, arr[p2])
        print(f"Reverse block: {reverse_block}")

        p1 = find_first_opening(arr, reverse_block)
        print(f"First opening: {p1}")

        if p1 >= p2:
            p2 -= reverse_block
            continue

        if p1 == -1:
            p2 -= reverse_block
            continue

        for j in range(reverse_block):
            temp = arr[p1 + j]
            arr[p1 + j] = arr[p2 - j]
            arr[p2 - j] = temp

    print(arr)

    sum = 0
    for i in range(len(arr)):
        if arr[i] == -1:
            continue
        sum += i * arr[i]

    print(sum)


main()
