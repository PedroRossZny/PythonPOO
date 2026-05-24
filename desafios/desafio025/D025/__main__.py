from rich import print
from rich.table import Table
from caminhao import Caminhao
from moto import Moto
from drone import Drone

def main():
    dist = 20

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    tabela = Table(title="\n[cyan]Tabela de Fretes[/]", style="cyan")

    tabela.add_column("[blue]Distancia[/]", justify="left")
    tabela.add_column("[yellow]Tipo[/]", justify="left")
    tabela.add_column("[green]Frete[/]", justify="left")

    for l in range(len(viagem)):
        tabela.add_row(f"[blue]{dist}Km[/]", f"[yellow]{type(viagem[l]).__name__}[/]", f"{viagem[l].calc_frete()}")

    print(tabela)


if __name__ == "__main__":
    main()