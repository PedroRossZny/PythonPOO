from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        pesototal = self.quant * 0.4
        custototal = pesototal * 82.4
        custocada = custototal / self.quant
        painel = Panel(f"[white]Analisando [yellow]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n"
                       f"Cada participante comerá [red]0.4Kg[/] e cada Kg custa [green]R$82.40[/]\n"
                       f"Recomendo [red]comprar {pesototal:.3f}Kg[/] de carne\n"
                       f"O custo total sera de [green]R${custototal:.2f}[/]\n"
                       f"Cada pessoa pagara [green]R${custocada:.2f}[/] para participar.[/]", title=f"{self.titulo}", style="bold yellow")
        print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()