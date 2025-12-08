import numpy as np

from util import next_int, next_line, next_line_ints, next_word, read_whole


def solve_system_of_equations(A, b):
    """
    Solves the system of linear equations Ax = b for positive integer solutions.

    Parameters:
    A (2D array): Coefficient matrix
    b (1D array): Constant terms

    Returns:
    x (tuple): Solution to the system of equations (x, y)
    """
    a1, b1 = A[0]
    a2, b2 = A[1]
    c1, c2 = b

    # Brute-force approach to find positive integer solutions
    for x in range(1, 100000):  # Adjust the range as needed
        for y in range(1, 100000):  # Adjust the range as needed
            if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
                return (x, y)
    return None


def main():
    for i in range(320):
        l1 = next_line().split(' ')
        l2 = next_line().split(' ')
        l3 = next_line().split(' ')
        col11 = int(l1[2].split('+')[1][:-1])
        col12 = int(l1[3].split('+')[1])
        col21 = int(l2[2].split('+')[1][:-1])
        col22 = int(l2[3].split('+')[1])
        target1 = int(l3[1].split('=')[1][:-1])
        target2 = int(l3[2].split('=')[1])

        A = [[col11, col21], [col12, col22]]
        b = [target1, target2]

        x = solve_system_of_equations(A, b)

        print(x[0], x[1])

        next_line()

    pass


main()
