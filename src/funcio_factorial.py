def factorial(n):
    if not isinstance(n, int):
        raise TypeError("El factorial solo puede calcularse para enteros")
    if n < 0:
        raise ValueError("El factorial no está definido para enteros negativos")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
