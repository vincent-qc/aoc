# Define the file path
# file_path = 'data/input.txt'
file_path = 'data/input.txt'

# Open the file and store the file object as a global variable
file = open(file_path, 'r')


def read_whole():
    content = file.read()
    file.seek(0)  # Reset file pointer to the beginning after reading
    return content.split()


def next_word():
    word = ''
    while True:
        char = file.read(1)
        if char.isspace() or char == '':
            break
        word += char

    if word == '':
        return next_word()
    return word


def next_int():
    word = next_word()
    return int(word)


def next_line():
    return file.readline().strip()


def next_line_ints(delimiter=" "):
    return list(map(int, next_line().split(delimiter)))


# Define the output file path
output_file_path = 'data/output.txt'


def print_int(value):
    with open(output_file_path, 'a') as file:
        file.write(f"{value} ")


def print_word(word):
    with open(output_file_path, 'a') as file:
        file.write(f"{word} ")


def print_line(line):
    with open(output_file_path, 'a') as file:
        file.write(f"{line}\n")
