import pytest
from resources.maths_operations import hello_world, add, subtract, multiply

def test_hello_world():
    """
    This function tests the hello_world function
    :return:  "Hello World"
    """
    assert hello_world() == "Hello World"

def test_hello_world():
    """
    This function tests the hello_world function
    :return:  "Hello World"
    """
    assert hello_world() == "Hello Worlds"

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    """
    This function tests the add function
    :param a:
    :param b:
    :param expected:
    :return:
    """
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (10, 10, 0),
    (-2, -2, 0),
    (0, 5, -5),
])
def test_subtract(a, b, expected):
    """
    This function tests the subtract function
    :param a:
    :param b:
    :param expected:
    :return:
    """
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (0, 10, 0),
    (5, 5, 25),
])
def test_multiply(a, b, expected):
    """
    This function tests the multiply function
    :param a:
    :param b:
    :param expected:
    :return:
    """
    assert multiply(a, b) == expected
