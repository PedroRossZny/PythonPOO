from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa come em media 400g de carne
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self, titulo, quant):
        # Atributos de Instancia
        self.titulo = titulo
        self.participantes = quant

    def __str__(self):
        return f"Esse e {self.titulo} com {self.participantes} pessoas participando."

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.participantes} convidados[/]"
        conteudo += f"\nCada participante comera {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total sera de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagara [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
c2.analisar()