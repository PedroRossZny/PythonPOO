from poligono import *

class Quadrado(Poligono):
    def __init__(self, lado, qtd_lados = 4):
        super().__init__(qtd_lados)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2