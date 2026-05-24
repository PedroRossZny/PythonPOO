from abc import ABC, abstractmethod
from rich import print

class BebidaQuente(ABC):
    def preparar(self):
        print("[blue bold]--- Iniciando o Preparo ---[/]\n"
              f"[red bold]1.[/] {self.ferver_agua()}\n"
              f"[yellow bold]2.[/] {self.misturar()}\n"
              f"[green bold]3.[/] {self.servir()}\n"
              "[blue bold]--- Bebida Pronta ---[/]")

    def ferver_agua(self) -> str:
        return "Fervendo agua a 100 graus Celsius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass