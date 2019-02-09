import sys

import numpy as np
from io import StringIO

USAGE = """
Program for solving n-element linear equations

Usage:
    {program} [--test|--exercise-file <filepath>]
    
Where:
    filepath - is text file containing matrix of elements of equation in form:
n
A11 A12...A1n b1
...
An1.......Ann bn
"""


def read_exercise_from_text(text):
    c = StringIO(text.strip())
    size = int(c.readline())  # read size from first line

    data = np.loadtxt(c, dtype=int, unpack=True)  # load rest of the data to array and transpose it (unpack = True)
    A = np.transpose(data[0: -1])  # 2D array of parameters
    b = data[-1]  # 1D array of results
    return size, A, b


# https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve
def solve_linear_equation(A, b):
    if len(A) > 1:
        return np.linalg.solve(A, b)
    else:
        return b[0] / A[0]


def read_exercise_from_file(fpath):
    with open(fpath) as fp:
        return read_exercise_from_text(fp.read())


def check_solution(A, b, solution):
    return np.allclose(np.dot(A, solution), b)


def exercise(exercise_reader):
    size, A, b = exercise_reader()
    print("A:")
    print(A)
    print('b:')
    print(b)

    x = solve_linear_equation(A, b)
    print('Result=')
    print(x)

    test_result = np.allclose(np.dot(A, x), b)
    print('Passes test:', test_result)


def test():
    text = """
    3
    1 2 3 7
    -1 2 4 6
    2 1 1 13
    """
    ex_reader = lambda: read_exercise_from_text(text)
    exercise(ex_reader)


def usage():
    usage_txt = USAGE.format(program=sys.argv[0])
    print(usage_txt)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
    else:
        command = sys.argv[1]
        if command == "--test":
            test()
        elif command == "--exercise-file":
            fpath = sys.argv[2]
            reader = lambda: read_exercise_from_file(fpath)
            exercise(reader)
