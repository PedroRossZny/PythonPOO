from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia, frete):
        self.distancia = distancia
        self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass