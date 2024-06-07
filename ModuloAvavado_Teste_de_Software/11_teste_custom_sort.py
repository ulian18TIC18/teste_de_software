import pytest

def custom_sort(numbers):
    return sorted(numbers, reverse=True)

def teste_custom_sort():
    num = [12, 7, 4, 18, 13, 0]
    ordem_reversa = [18, 13, 12, 7, 4, 0]
    assert custom_sort(num) == ordem_reversa

    num1 = [-20, -30, -4, 0 , 5, -1]
    ordem_reversa2 = [5, 0, -1, -4, -20, -30]
    assert custom_sort(num1) == ordem_reversa2