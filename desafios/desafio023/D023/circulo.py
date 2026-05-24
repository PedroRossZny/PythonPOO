from poligono import *
from math import pi

class Circulo(Poligono):
    def __init__(self, raio, qtd_lados = 0):
        super().__init__(qtd_lados)
        self.raio = raio

    def perimetro(self):
        return 2 * self.raio * pi

    def area(self):
        return pi * self.raio ** 2