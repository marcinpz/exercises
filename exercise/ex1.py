import numpy as np

from io import StringIO


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
    return (size, data) if len(data) > 0 and isinstance(data[0], list) else (size, [data])


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


def solve_linear_equation(data):
    np_data = np.array(data)
    X, y = np_data[:, :-1], np_data[:, -1]
    error = check_linear_equation_errors(np_data)
    return (error, None) if error else (None, np.linalg.solve(X, y))
    # try:
    #     result = np.linalg.solve(X, y)
    # except np.linalg.LinAlgError as er:
    #     error = er
    # return error, result
