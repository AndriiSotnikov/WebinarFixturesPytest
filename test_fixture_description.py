"""
In Pytest, fixtures can be defined and stored in several places, depending on how you want to use them and what level of 
scope you need. 

1. In a conftest.py file: 
Fixtures can be defined in a file named conftest.py located in the root directory of your test suite or in any of its
 subdirectories. 
Any fixture defined in a conftest.py file will automatically be available to all the test files located in the same 
directory or its subdirectories. 
This is a good way to share fixtures across multiple test files.

2. In a test file: 
Fixtures can also be defined in a test file itself. 
These fixtures will only be available within that particular test file, and will not be available to other test files. 
This can be useful if you only need a fixture for a specific set of tests.

3. In a fixture file: 
Fixtures can also be defined in a separate Python file and then imported into the test files that need them. 
This approach allows you to organize your fixtures separately from your test files, which can be useful if you have a 
large number of fixtures or if you want to reuse fixtures across multiple test suites.
"""


import pytest

@pytest.fixture(scope="function")
def my_function_fixture():
    print("\nSetup for function-level fixture")
    yield
    print("\nTeardown for function-level fixture")

@pytest.fixture(scope="class")
def my_class_fixture():
    print("\nSetup for class-level fixture")
    yield
    print("\nTeardown for class-level fixture")

@pytest.fixture(scope="module")
def my_module_fixture():
    print("\nSetup for module-level fixture")
    yield
    print("\nTeardown for module-level fixture")

@pytest.fixture(scope="session")
def my_session_fixture():
    print("\nSetup for session-level fixture")
    yield
    print("\nTeardown for session-level fixture")

class TestMyClass:
    def test_my_function(self, my_function_fixture):
        print("Running test_my_function")

    def test_another_function(self, my_function_fixture):
        print("Running test_another_function")

def test_module_level_fixture(my_module_fixture):
    print("Running test_module_level_fixture")

def test_session_level_fixture(my_session_fixture):
    print("Running test_session_level_fixture")
