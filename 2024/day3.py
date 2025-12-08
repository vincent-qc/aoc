from util import next_int, next_line, next_line_ints, next_word, read_whole


def main():
    sum = 0
    should_mul = True
    for _ in range(6):
        line = next_line()

        for i in range(len(line) - 3):
            is_do = line[i:i+4] == "do()"
            is_dont = line[i:i+7] == "don't()"

            if is_do:
                should_mul = True
            if is_dont:
                should_mul = False

            if not should_mul:
                continue

            is_mul = line[i:i+3] == "mul"

            if not is_mul:
                continue

            if line[i+3] != '(':
                continue

            index_of_end_para = line.find(')', i+3)
            para_contents = line[i+4:index_of_end_para].split(",")

            if len(para_contents) != 2:
                continue

            if not para_contents[0].isnumeric() or not para_contents[1].isnumeric():
                continue
            cont1 = int(para_contents[0])
            cont2 = int(para_contents[1])

            sum += cont1 * cont2

    print(sum)


main()
