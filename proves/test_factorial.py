import pytest
from ci_factorial.src.funcio_factorial import factorial


def test_factorial_de_1():
    assert factorial.factorial(1) == 1


def test_factorial_type_error():
    with pytest.raises(TypeError):
        factorial.factorial(2.5)


def test_factorial_value_error():
    with pytest.raises(ValueError):
        factorial.factorial(-3)


def test_factorial_de_5():
    assert factorial.factorial(5) == 120
