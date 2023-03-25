"""
1. -k EXPRESSION or --keyword EXPRESSION: 
pytest -k "expression"
This allows you to select tests based on a keyword expression. 

2. -m MARKEXPR or --markexpr MARKEXPR: 
pytest -m marker_name
This allows you to select tests based on their markers. 

3. path/to/test_file.py::test_function: 
This allows you to select a specific test function to run within a test file. 
pytest tests/test_login.py::test_login.

4. -x or --exitfirst: 
This stops the test run after the first failure or error is encountered. 

5. -v or --verbose: This increases the verbosity of the output

6. --last-failed: This re-runs only the tests that failed in the previous test run.

7. --failed-first: This runs all tests, but the failed tests are run first.

8. Running tests in parallel: 
 -n option followed by the number of processes to run tests in parallel.

 NOTE: pip install pytest-xdist

 pytest -n 4 

"""

import time
import pytest

@pytest.mark.parametrize("test_input", list(range(10)))
def test_wait_for_value(test_input):
    #pytest test_pytest_run_options.py::test_wait_for_value
    #pytest -n 5 test_pytest_run_options.py::test_wait_for_value
    time.sleep(3)
    assert True


@pytest.mark.parametrize("value", list(range(1, 11)))
def test_odd_even(value):
    #pytest test_pytest_run_options.py::test_odd_even
    #pytest -v -k "5 or 6" test_pytest_run_options.py::test_odd_even
    if value % 2 == 0:
        assert value % 2 == 2, "This number is not even"  
    else:
        assert value % 2 == 1, "This number is not odd"




# pytest -m marker2
# pytest -m "marker1 and marker2"
# pytest -m "marker1 or marker2"
@pytest.mark.parametrize("value", [1, 2, 3, 4])
@pytest.mark.marker1
def test_even(value):
    assert value % 2 == 0

@pytest.mark.parametrize("value", [5, 6, 7, 8])
@pytest.mark.marker2
def test_odd(value):
    assert value % 2 == 1

@pytest.mark.parametrize("value", [9, 10, 11, 12])
@pytest.mark.marker1
@pytest.mark.marker2
def test_even(value):
    assert value % 2 == 0
