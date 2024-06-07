import pytest

def factorial(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def teste_fatorial_limites():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(10) == 3628800

    with pytest.raises(ValueError):
        factorial(-1)

    with pytest.raises(ValueError):
        factorial(-10)
