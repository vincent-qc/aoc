from util import next_int, next_line, next_line_ints, next_word, read_whole


def get_middle(arr):
    return arr[int(len(arr)/2)]


def main():
    before = [set() for _ in range(100)]

    for _ in range(1176):
        line = next_line()
        parts = line.split("|")
        n1 = int(parts[0])
        n2 = int(parts[1])
        before[n2].add(n1)

    next_line()

    count = 0
    for i in range(1178, 1369):
        pages = next_line_ints(",")
        is_valid = True
        print(pages)
        k = 0
        while k < len(pages):
            page = pages[k]
            for j in range(len(pages[k:])):
                next = pages[k:][j]
                if next in before[page]:
                    index_next = pages.index(next)
                    pages[k] = next
                    pages[index_next] = page
                    is_valid = False
                    print(pages)
                    k -= 1
                    break
            k += 1
        if not is_valid:
            print(pages, "\n\n")
            count += get_middle(pages)
        else:
            print('\n\n')

    print(count)
    pass


main()
