import pytest

from exercise import ex2


@pytest.mark.parametrize("x, expected_result", [
    (153, True),
    (1, True),
    (10, False)
])
def test_is_amstrong_number(x, expected_result):
    assert expected_result == ex2.is_amstrong_number(x)
