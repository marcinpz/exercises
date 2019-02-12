import pytest
import numpy as np

from exercise import ex1


@pytest.mark.parametrize("test_input,size,a", [
    ("""
3
1 2 3 7
-1 2 4 6
2 1 1 13
""",
     3,
     [[1, 2, 3, 7],
      [-1, 2, 4, 6],
      [2, 1, 1, 13]]),
    ("""
2
1 2 3
3 4 5
""",
     2,
     [[1, 2, 3],
      [3, 4, 5]]),
    ("""
1
2 1
""",
     1,
     [[2, 1]])
])
def test_read_exercise_from_text(test_input, size, a):
    _size, _a = ex1.read_exercise_from_text(test_input)

    assert size == _size
    assert np.shape(a) == _a.shape
    np.allclose(a, _a)


@pytest.mark.parametrize("data, expected_result", [
    (
            [[1, 2, 3, 7],
             [-1, 2, 4, 6],
             [2, 1, 1, 13]],
            [18, -58, 35]
    ), (
            [[1, 2, 3],
             [3, 4, 5]],
            [-1, 2]),
    ([[1, 2]],
     [2])
])
def test_solve_linear_equation__one_solution(data, expected_result):
    err, result = ex1.solve_linear_equation(np.array(data))
    assert err is None
    assert np.allclose(result, expected_result)


@pytest.mark.parametrize("data", [
    [[0, 2]],
    [[1, 1, 1],
     [2, 2, 4]],
])
def test_solve_linear_equation__no_solution(data):
    err, result = ex1.solve_linear_equation(np.array(data))
    assert isinstance(err, ex1.LinEquationNoSolutionError)
    assert result is None


@pytest.mark.parametrize("data", [
    [[0, 0]],
    [[1, 1, 1],
     [2, 2, 2]],
    [[1, 3, 2],
     [1, 3, 2]]
])
def test_solve_linear_equation__infinite_solutions(data):
    err, result = ex1.solve_linear_equation(np.array(data))
    assert isinstance(err, ex1.LinEquationMultipleSolutionsError)
    assert result is None


@pytest.mark.parametrize("a, expected_result", [
    ([[0, 1], [0, 2]], 1),
    ([[0, 1], [1, 3]], 2),
    ([[0, 1, 2], [0, 1, 2]], 1),
    ([[1]], 1)
])
def test_get_independent_matrix_rows(a, expected_result):
    assert ex1.get_independent_matrix_rows(np.array(a)) == expected_result


@pytest.mark.parametrize("data, x, y", [
    ([[0, 0]], [[0]], [0]),
    ([[1, 1, 1],
      [2, 2, 2]],
     [[1, 1],
      [2, 2]],
     [1, 2])
])
def test_data_to_xy(data, x, y):
    _x, _y = ex1.data_to_xy(np.array(data))
    assert _x.shape == np.shape(x)
    assert _y.shape == np.shape(y)
    assert np.allclose(_x, x)
    assert np.allclose(_y, y)
