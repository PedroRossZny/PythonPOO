from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas, atual=1):
        self.titulo = titulo
        self.paginas = paginas
        self.atual = atual

        print(f":book: [blue]Voce acabou de abrir o livro '[red]{self.titulo}[/]' que tem [bold green]{self.paginas}[/][green] paginas[/] no total.[/]\n"
              f"[blue]Voce agora esta na [yellow]pagina [bold]{self.atual}[/]")

    def avancar_paginas(self, quant):
        if self.atual + quant <= self.paginas:
            for i in range(quant):
                print(f"Pag{self.atual + 1} :arrow_forward:", end=" ")
                sleep(0.5)
                self.atual += 1
            print(":round_pushpin:")
            print(f"[blue]Voce avancou [bold]{quant}[/][blue] paginas e agora esta na [yellow]pagina [bold]{self.atual}[/]")
        else:
            quant = self.paginas - self.atual
            for i in range(self.paginas - self.atual):
                print(f"Pag{self.atual + 1} :arrow_forward:", end=" ")
                sleep(0.5)
                self.atual += 1
            print(":x: ")
            print(f"[blue]Voce avancou [bold]{quant}[/][blue] e agora esta na [yellow]pagina [bold]{self.atual}[/]\n"
                  f":closed_book: [red]Voce chegou ao final do livro '[bold]10 coisas que aprendi[/]'[/]")

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
