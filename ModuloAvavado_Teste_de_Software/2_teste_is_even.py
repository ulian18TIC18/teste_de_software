import pytest

def is_even(number):
    """Função que verifica se um número é par."""
    return number % 2 == 0


def test_is_even_with_even_number():
    assert is_even(4) == True

def test_is_even_with_odd_number():
    assert is_even(5) == False

def test_is_even_with_zero():
    assert is_even(0) == True