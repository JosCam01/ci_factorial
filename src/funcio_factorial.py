"""
funcio_factorial module
A simple module to calculate the factorial of a non-negative integer.
"""


def factorial(numero):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The integer to calculate the factorial for.

    Returns:
        int: The factorial of the input integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(numero, int):
        raise TypeError("El factorial solo puede calcularse para enteros")
    if numero < 0:
        raise ValueError("El factorial no está definido para enteros negativos")
    result = 1
    for i in range(1, numero + 1):
        result *= i
    return result
