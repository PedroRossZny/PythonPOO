from rich import print
from transporte import *

class Caminhao(Transporte):
    def __init__(self, distancia, fator = 1.2, frete = 0):
        super().__init__(distancia, frete)
        self.fator = fator

    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = self.fator * self.distancia
            return f"[green bold]R${self.frete:.2f}[/]"
        else:
            return "[red bold]Raio minimo de 50Km[/]"