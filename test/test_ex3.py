import pytest

from exercise import ex3


@pytest.mark.parametrize("x, expected_result", [
    (153, False),
    (1, True),
    (11, True),
    (121, True)
])
def test_is_palindrom(x, expected_result):
    assert expected_result == ex3.is_palindrom(x)


@pytest.mark.parametrize("x", [153, 1, 11, 121])
def test_check_hyphotesis_is_true__works(x):
    assert ex3.check_hyphotesis_is_true(x, 10) is True


@pytest.mark.xfail
def test_check_hyphotesis_is_true__does_not_work():
    assert ex3.check_hyphotesis_is_true(196, 10000) is True
