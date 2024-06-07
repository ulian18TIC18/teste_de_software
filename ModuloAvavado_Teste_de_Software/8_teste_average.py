import pytest

def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    return sum(numbers) / len(numbers)

def teste_calculo_media_positivos():
    num = [1, 2, 3, 4, 5]
    assert calculate_average(num) == 3

    with pytest.raises(ValueError):
        calculate_average([])

def teste_calculo_media_negativos():
    num = [-5, -4, -3, -2, -1]   
    assert calculate_average(num) == -3

def teste_calculo_media_um_numero():
    num = [20]
    assert calculate_average(num) == 20

def teste_calculo_media_zero():
    num = [0]
    assert calculate_average(num) == 0

def teste_calculo_media_float():
    num = [1.1, 2.2, 3.3, 4.4, 5.5]
    assert calculate_average(num) == 3.3

def teste_calculo_media_float_negativo():
    num = [-1.1, -2.2, -3.3, -4.4, -5.5]
    assert calculate_average(num) == -3.3

def teste_calculo_media_numero_grandes():
    num = [1000000000000, 2000000000000, 3000000000000, 4000000000000, 5000000000000]   
    assert calculate_average(num) == 3000000000000

def teste_calculo_media_numero_negativos_grandes():
    num = [-1000000000000, -2000000000000, -3000000000000, -4000000000000, -5000000000000]   
    assert calculate_average(num) == -3000000000000