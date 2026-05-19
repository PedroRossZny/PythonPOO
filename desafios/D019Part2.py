from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Voce acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.total_paginas} paginas[/] no total. Voce agora esta na [yellow]pagina {self.pagina_atual}[/][/blue]")

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pag{self.pagina_atual} :arrow_forward: ", end='')
                time.sleep(0.3)
                cont += 1
        print(f"[blue]Voce avancou {cont} paginas e agora esta na [yellow]pagina {self.pagina_atual}[/][/blue]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Voce chegou ao final do livro '{self.titulo}'[/red]")

    def fim_do_livro(self) -> bool:
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro("10 coisas de aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)