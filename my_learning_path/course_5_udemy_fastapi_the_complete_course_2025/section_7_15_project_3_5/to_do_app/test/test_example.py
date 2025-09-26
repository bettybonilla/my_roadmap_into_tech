"""
The below shows some unit testing basics with pytest
"""

import pytest


# Validates equal or not equal
def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1
    # If you uncomment it will fail this unit test since all assert statements must pass within the function
    # assert 3 == 1


# Validates instances
def test_instance():
    assert isinstance("this is a string", str)
    assert not isinstance("10", int)


# Validates booleans
def test_boolean():
    validated = True
    assert validated is True
    assert ("hello" == "world") is False


# Validates types
def test_type():
    assert type("hello" is str)
    assert type("world" is not int)


# Validates greater than or less than
def test_greater_than_or_less_than():
    assert 7 > 3
    assert 4 < 10


# Validates lists
def test_list():
    num_list = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, year: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.year = year


# Validates objects
# def test_student():
#     person = Student("John", "Doe", "Computer Science", 3)
#     # You can pass in an optional message as a second argument with your assert statements
#     assert person.first_name == "John", "First name should be John"
#     assert person.last_name == "Doe", "Last name should be Doe"
#     assert person.major == "Computer Science", "test"
#     assert person.year == 3


# Refactored code
# Instead of defining a unit test for every object that gets created like in the commented out code above, we can use
# the @pytest.fixture decorator to re-use objects as parameterized fixture values for our unit tests
# Fixtures are a convenient way of implementing setUp and tearDown methods
# They are defined using the @pytest.fixture decorator and pytest has several useful built-in fixtures
# Below, you can pass in the object the fixture returns as a parameterized fixture value to a unit test similar to how
# you would implement a setUp() method
@pytest.fixture
def mock_student() -> Student:
    # You don't need to instantiate the Student class with a variable
    return Student("John", "Doe", "Computer Science", 3)


# Validates objects
# When pytest goes to run a test, it looks at the parameters in that test function’s signature, and then searches for
# fixtures that have the same names as those parameters
# Once pytest finds them, it runs those fixtures, captures what they returned (if anything), and passes those objects
# into the test function as arguments
def test_student(mock_student):
    assert mock_student.first_name == "John", "First name should be John"
    assert mock_student.last_name == "Doe", "Last name should be Doe"
    assert mock_student.major == "Computer Science", "test"
    assert mock_student.year == 3
