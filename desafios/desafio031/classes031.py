from rich import print

class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = base
        self._altura = altura
        self._area = None

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @property
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @property
    def medidas(self):
        return (f"[blue]Base = [yellow]{self._base}[/]\n"
                f"[blue]Altura = [yellow]{self._altura}[/]\n"
                f"[blue]Area = [yellow]{self._area}[/]")

    @altura.setter
    def altura(self, altura):
        if altura >= 0:
            self._altura = altura
        else:
            raise ValueError("Valor invalido para altura")

    @base.setter
    def base(self, base):
        if base >= 0:
            self._base = base
        else:
            raise ValueError("Valor invalido para base")

    @medidas.setter
    def medidas(self, medidas = (1, 1)):
        self._base = medidas[0]
        self._altura = medidas[1]
        self._area = self._base * self._altura
