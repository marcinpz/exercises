import numpy as np

from io import StringIO


def read_exercise_from_text(text):
    c = StringIO(text.strip())
    size = int(c.readline())  # read size from first line

    data = np.loadtxt(c, dtype=int)  # load rest of the data to array and transpose it (unpack = True)
    # return (size, data) and make sure data is 2d array even if there is only 1 row in file. It is needed by 'solve'
    return (size, data) if len(data) > 0 and isinstance(data[0], list) else (size, [data])


def solve_linear_equation(data):
    np_data = np.array(data)
    X, y = np_data[:, :-1], np_data[:, -1]
    error = result = None
    try:
        result = np.linalg.solve(X, y)
    except np.linalg.LinAlgError as er:
        error = er
    return error, result
