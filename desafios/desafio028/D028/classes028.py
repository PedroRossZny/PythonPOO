from rich import print

class Termostato:
    def __init__(self, temperatura = 24):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @property
    def ftemperatura(self):
        return f"[yellow bold]{self.__temperatura}°C[/]"

    @temperatura.setter
    def temperatura(self, graus):
        if graus % 0.5 != 0:
            raise ValueError(f"Temperatura de {graus}°C e invalida!")
        elif graus < 16:
            self.__temperatura = 16
        elif graus > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = graus
