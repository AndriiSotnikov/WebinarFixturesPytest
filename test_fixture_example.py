import pytest

@pytest.fixture
def list_of_numbers():
    return [1, 2, 3, 4, 5]
    
def test_calculate_sum(list_of_numbers):
    assert sum(list_of_numbers) == 15

def test_calculate_mean(list_of_numbers):
    assert sum(list_of_numbers) / len(list_of_numbers) == 3
