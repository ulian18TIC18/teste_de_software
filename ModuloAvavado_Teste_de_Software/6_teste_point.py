import pytest
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise ValueError("Argument must be a Point")
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def teste_distance_to_zero():
    ponto1 = Point(0, 0)
    ponto2 = Point(0,0)
    assert ponto1.distance_to(ponto2) == 0

def test_distance_to_another_point():
    ponto1 = Point(0, 0)
    ponto2 = Point(3, 4)
    assert ponto1.distance_to(ponto2) == 5

def test_distance_to_non_point():
    ponto1 = Point(0, 0)
    with pytest.raises(ValueError):
        ponto1.distance_to("not a point")


