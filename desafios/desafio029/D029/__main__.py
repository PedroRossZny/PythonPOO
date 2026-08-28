from classes029 import Diario
from rich import print, inspect

def main():
    d = Diario("Gafanhoto")

    d.escrever("Primeira mensagem")
    d.escrever("Voce e uma pessoa simpatica")
    d.escrever("Voce gosta de Python")

    d.ler("Gafanhoto")

    # inspect(d, private=True, methods=True)

if __name__ == '__main__':
    main()
