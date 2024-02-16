import pytest
import src.funcio_factorial as funcio_factorial


def test_factorial_de_1():
    assert funcio_factorial.factorial(1) == 1


def test_factorial_type_error():
    with pytest.raises(TypeError):
        funcio_factorial.factorial(2.5)


def test_factorial_value_error():
    with pytest.raises(ValueError):
        funcio_factorial.factorial(-3)


def test_factorial_de_5():
    assert funcio_factorial.factorial(5) == 120
