import pytest

class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somarNumeros(self):
        num1 = self.a
        num2 = self.b

        resultado_soma = num1 + num2

        print(f'A soma de {num1} + {num2} é igual a {resultado_soma}')
        return resultado_soma


    def divisaoNumeros(self):
        num1 = self.a
        num2 = self.b

        if num2 == 0:
            raise ZeroDivisionError("A divisãopor zero não é possível")

        else:
            resultado_divisao = num1 / num2

            print(f'a divisão de {num1} e {num2} é igual a {resultado_divisao}')
        
            return resultado_divisao



def test_somar_numeros_positivos():
    calculo = Calculadora(2, 3)
    assert calculo.somarNumeros() == 5

def test_dividir_numeros_decimais():
    caluclo = Calculadora(4.5, 1.5)
    assert caluclo.divisaoNumeros() == pytest.approx(3.0)

def test_dividir_por_zero():
    calculo = Calculadora(3.0, 0)
    try:
        calculo.divisaoNumeros()
    except ZeroDivisionError as exception:
        assert str(exception) == "A divisãopor zero não é possível"
        
