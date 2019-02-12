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


class LinEquationError:
    pass


class LinEquationNoSolutionError(LinEquationError):
    pass


class LinEquationMultipleSolutionsError(LinEquationError):
    pass


def read_exercise_from_text(text):
    c = StringIO(text.strip())
    size = int(c.readline())  # read size from first line

    data = np.loadtxt(c, dtype=int)  # load rest of the data to array and transpose it (unpack = True)
    # return (size, data) and make sure data is 2d array even if there is only 1 row in file. It is needed by 'solve'
    return (size, data.reshape((1, 2))) if data.ndim == 1 else (size, data)


def read_exercise_from_file(fpath):
    with open(fpath) as fp:
        return read_exercise_from_text(fp.read())


# http://kitchingroup.cheme.cmu.edu/blog/2013/03/01/Determining-linear-independence-of-a-set-of-vectors/
def get_tolerance(A):
    eps = np.finfo(np.linalg.norm(A).dtype).eps
    return max(eps * np.array(A.shape))


def get_independent_matrix_rows(A, tolerance=None):
    _tolerance = get_tolerance(A) if tolerance is None else tolerance
    u, s, v = np.linalg.svd(A)
    return np.sum(np.abs(s) > _tolerance)


# https://pl.wikipedia.org/wiki/Twierdzenie_Kroneckera-Capellego
# https://www.matmana6.pl/twierdzenie-kroneckera-capellego
def check_linear_equation_errors(np_data):
    X = np_data[:, :-1]
    det_data, det_x = list(map(get_independent_matrix_rows, [np_data, X]))
    n = X.shape[0]
    if det_data == det_x:
        if n == det_data:
            return None
        else:
            return LinEquationMultipleSolutionsError()
    else:
        return LinEquationNoSolutionError()


def data_to_xy(np_data):
    return np_data[:, :-1], np_data[:, -1]


def solve_linear_equation(np_data):
    X, y = data_to_xy(np_data)
    error = check_linear_equation_errors(np_data)
    return (error, None) if error else (None, np.linalg.solve(X, y))


def usage():
    usage_txt = USAGE.format(program=sys.argv[0])
    print(usage_txt)


def check_solution(A, b, solution):
    return np.allclose(np.dot(A, solution), b)


def exercise(exercise_reader):
    size, np_data = exercise_reader()
    A, b = data_to_xy(np_data)
    print("A:")
    print(A)
    print('\nb:')
    print(b)

    err, x = solve_linear_equation(np_data)
    if err is None:
        print('\nResult: ')
        print(x)

        print('\nPasses test:', check_solution(A, b, x))
    elif isinstance(err, LinEquationNoSolutionError):
        print("\nThere is no solution for that equation!")
    elif isinstance(err, LinEquationMultipleSolutionsError):
        print("\nThere is infinite number of solutions for that equation!")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        fpath = sys.argv[1]
        reader = lambda: read_exercise_from_file(fpath)
        exercise(reader)
    else:
        usage()
