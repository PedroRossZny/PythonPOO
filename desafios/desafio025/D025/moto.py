from rich import print
from transporte import *

class Moto(Transporte):
    def __init__(self, distancia, fator = 0.5, frete = 0):
        super().__init__(distancia, frete)
        self.fator = fator

    def calc_frete(self):
        self.frete = self.fator * self.distancia
        return f"[green bold]R${self.frete:.2f}[/]"