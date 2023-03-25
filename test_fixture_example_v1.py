"""
Useful links:
1. https://docs.pytest.org/en/latest/getting-started.html - pytest documentation
2. https://docs.pytest.org/en/latest/explanation/fixtures.html - pytest fixtures docs
"""


import pytest

@pytest.fixture
def multiple_by_two(number):
    return number * 2

@pytest.mark.parametrize("number", [2])
def test_calculation(multiple_by_two):
    assert multiple_by_two == 4

@pytest.mark.parametrize("number", [3.0])
def test_calculation_float(multiple_by_two):
    assert multiple_by_two == 6.0

@pytest.mark.parametrize("number", ['Two '])
def test_calculation_str(multiple_by_two):
    assert multiple_by_two == 'Two Two '


