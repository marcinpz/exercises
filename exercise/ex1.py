import sys

import numpy as np
from io import StringIO


def read_exercise_from_text(text):
    c = StringIO(text.strip())
    size = int(c.readline())  # read size from first line

    data = np.loadtxt(c, dtype=int, unpack=True)  # load rest of the data to array and transpose it (unpack = True)
    A = np.transpose(data[0: -1])  # 2D array of parameters
    b = data[-1]  # 1D array of results
    return size, A, b


# https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve
def solve_linear_equation(A, b):
    return np.linalg.solve(A, b)


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
    print("Usage:")
    print(f"{sys.argv[0]} [--test|--exercise-file <filepath>]")


if __name__ == '__main__':
    print(sys.argv, len(sys.argv))
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
