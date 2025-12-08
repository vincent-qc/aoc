from util import next_int, next_line, next_line_ints, next_word, read_whole

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def valid_pos(i, j):
    return 0 <= i < 50 and 0 <= j < 50


def add_to_map(char_map, i, j, char):
    if char not in char_map:
        char_map[char] = []
    char_map[char].append((i, j))


def main():
    grid = []
    chars = set()
    for _ in range(50):
        line = next_line()
        char_arr = []
        for c in line:
            chars.add(c)
            char_arr.append(c)
        grid.append(char_arr)

    char_map = {}
    for i in range(50):
        for j in range(50):
            if grid[i][j] == '.':
                continue
            add_to_map(char_map, i, j, grid[i][j])

    visited = [[False for _ in range(50)] for _ in range(50)]

    sum = 0
    for char in chars:
        if char not in char_map:
            continue

        positions = char_map[char]

        for i in range(len(positions)):
            for j in range(len(positions)):
                if i == j:
                    continue

                i1, j1 = positions[i]
                i2, j2 = positions[j]

                if char == 'A':
                    print("A:", i1, j1, i2, j2, "\n")

                idiff = i2 - i1
                jdiff = j2 - j1

                for k in range(100):
                    id, jd = i1 + k * idiff, j1 + k * jdiff

                    if not valid_pos(id, jd) or visited[id][jd]:
                        continue
                    visited[id][jd] = True
                    sum += 1

    print(sum)
    pass


main()
