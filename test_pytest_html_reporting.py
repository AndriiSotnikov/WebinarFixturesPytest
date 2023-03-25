"""
To use HTML reporting:

1. Install plugin: pip install pytest-html

2. To run test with report generation: pytest --html=report.html


"""

import pytest

def test_add():
    assert 1 + 1 == 2

def test_sub():
    assert 5 - 3 == 2

def test_mult():
    assert 2 * 2 == 4

def test_div():
    assert 10 / 2 == 5

@pytest.mark.parametrize("arg_1, arg_2, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (5, 5, 10),
])
def test_addition_param(arg_1, arg_2, expected):
    assert arg_1 + arg_2 == expected
