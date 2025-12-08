from util import next_int, next_line, next_line_ints, next_word, read_whole


def get_number_length(number):
    return len(str(number))


def try_number(number, length, dict):
    if length == 75:
        return 1
    if (str(number) + "#" + str(length)) in dict:
        print(str(number) + "#" + str(length))
        return dict[str(number) + "#" + str(length)]
    if number == 0:
        next = try_number(1, length + 1, dict)
        dict[number] = next
        return next
    elif (get_number_length(number) % 2) == 0:
        half = int((get_number_length(number) / 2))
        first_half = int(str(number)[:half])
        second_half = int(str(number)[half:])
        next = try_number(first_half, length + 1, dict) + \
            try_number(second_half, length + 1, dict)
        dict[str(number) + "#" + str(length)] = next
        return next
    else:
        next = try_number(number * 2024, length + 1, dict)
        dict[str(number) + "#" + str(length)] = next
        return next


def main():
    line = next_line_ints()
    dict = {}
    sum = 0
    for number in line:
        sum += try_number(number, 0, dict)
    print(sum)
    print("HERE")


main()
