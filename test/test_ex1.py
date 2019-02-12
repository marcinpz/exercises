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
    res = ex1.read_exercise_from_text(test_input)
    _size, _a = res

    assert size == _size
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
    err, result = ex1.solve_linear_equation(data)
    assert err is None
    assert np.allclose(result, expected_result)


@pytest.mark.parametrize("data, expected_result", [
    ([[0, 2]], None),
    (
            [[1, 1, 1],
             [2, 2, 4]],
            None
    )
])
def test_solve_linear_equation__no_solution(data, expected_result):
    err, result = ex1.solve_linear_equation(data)
    assert isinstance(err, np.linalg.LinAlgError)

