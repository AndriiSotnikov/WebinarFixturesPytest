"""Fixture parametrization in Pytest allows you to define a fixture that takes parameters and provide values 
for those parameters when using the fixture.
This can be useful when you have a fixture that needs to be used with different input data or configurations."""

import pytest

@pytest.fixture(params=[1, 2, 3])
def my_fixture(request):
    value = request.param
    print(f"\nSetting up fixture with value: {value}")
    yield value
    print(f"\nTearing down fixture with value: {value}")

def test_my_fixture(my_fixture):
    print(f"\nTesting with fixture value: {my_fixture}")
