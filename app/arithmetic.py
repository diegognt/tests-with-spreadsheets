def add(a: int, b: int) -> int:
    """
    Add a and b.

    Args:
        a: The first number
        b: The second number
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtract b from a.

    Args:
        a: The first number
        b: The second number
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiply a by b.

    Args:
        a: The first number
        b: The second number
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divide a by b.

    Args:
        a: The first number
        b: The second number
    Raises:
        ValueError: If b is 0
    """
    if b == 0:
        raise ValueError("Can not divide by 0")

    return a / b
