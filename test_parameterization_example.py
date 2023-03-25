import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10),
    (4, 9, 12)
])
def test_addition(a, b, expected):
    assert a + b == expected
