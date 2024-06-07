import pytest

class Atividades:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        num1 = self.a
        num2 = self.b
        
        resultado_soma = num1 + num2

        print(f'A soma de {num1} + {num2} é igual a {resultado_soma}')
        return resultado_soma

def test_add_deve_somar_numeros_positivos():
    calculo = Atividades(2, 5)
    assert calculo.add() == 7

def test_add_deve_somar_numero_positivo_negativo():
    calculo = Atividades(-1, 1)
    assert calculo.add() == 0

def test_add_deve_somar_numeros_negativos():
    calculo = Atividades(-2, -5)
    assert calculo.add() == -7
