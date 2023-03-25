"""
In Pytest, you can specify the scope of a fixture using the @pytest.fixture(scope="...") decorator. The available fixture scopes are:

1. "function" (default): The fixture is scoped to the test function. This means that the fixture is called once per test function that uses it.
2. "class": The fixture is scoped to the test class. This means that the fixture is called once per test class that uses it.
3. "module": The fixture is scoped to the test module. This means that the fixture is called once per module that uses it.
4. "session": The fixture is scoped to the entire test session. This means that the fixture is called once for the entire test run, regardless of how many test functions, classes, or modules use it.
"""


import pytest

@pytest.fixture(scope="function", autouse=True)
def my_function_fixture():
    print("\nSetup for function-level fixture")
    yield
    print("\nTeardown for function-level fixture")

@pytest.fixture(scope="class", autouse=True)
def my_class_fixture():
    print("\nSetup for class-level fixture")
    yield
    print("\nTeardown for class-level fixture")

@pytest.fixture(scope="module", autouse=True)
def my_module_fixture():
    print("\nSetup for module-level fixture")
    yield
    print("\nTeardown for module-level fixture")

@pytest.fixture(scope="session", autouse=True)
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
