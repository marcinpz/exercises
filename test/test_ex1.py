import pytest
import numpy as np

from exercise import ex1


@pytest.mark.parametrize("test_input,size,a,b", [
    ("""
3
1 2 3 7
-1 2 4 6
2 1 1 13
""",
     3,
     [[1, 2, 3],
      [-1, 2, 4],
      [2, 1, 1]],
     [7, 6, 13]),
    ("""
2
1 2 3
3 4 5
""",
     2,
     [[1, 2],
      [3, 4]],
     [3, 5]),
    ("""
1
2 1
""",
     1,
     [2],
     [1])
])
def test_read_exercise_from_text(test_input, size, a, b):
    _size, _a, _b = ex1.read_exercise_from_text(test_input)

    assert size == _size
    np.allclose(a, _a)
    np.allclose(b, _b)


def test_check_solution():
    pass
