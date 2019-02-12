import pytest

from exercise import ex4


@pytest.mark.parametrize("x, expected_result", [
    (2, [2]),
    (3, [2, 3]),
    (5, [2, 3, 5]),
    (10, [2, 3, 5, 7])
])
def test_eratostene_sieve(x, expected_result):
    assert ex4.eratostene_sieve(x) == expected_result


@pytest.mark.parametrize("x", [0, 1])
def test_eratostene_sieve(x):
    with pytest.raises(AssertionError):
        ex4.eratostene_sieve(x)
