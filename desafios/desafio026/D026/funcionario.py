from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome = "", sal_bruto = None, salario = None):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        print(Panel(f"O salario de [blue]{self.nome}[/] ([magenta]{self.__class__.__name__}[/]) e de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario / self.sal_min:.1f} salarios minimos[/].", title="Analise de Salario", width=50))