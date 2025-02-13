def hello_world() -> str:
    return "Hello World"


def add(a: int, b: int) -> int:
    """
    This function adds two numbers together
    :param a: an integer
    :param b: an integer
    :return: sum of a and b
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    This function subtracts two
    :param a: an integer
    :param b: an integer
    :return: sum of a minus b
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    This function multiplies two numbers
    :param a: an integer
    :param b: an integer
    :return: multiplies a and b
    """
    return a * b

def do_something(a: int, b: int, c: int) -> int:
    """
    Does something
    """
    result = a + b + c

    if result < 0:
        return 0
    return result
