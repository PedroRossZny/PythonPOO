from classe032 import ContaBancaria
from rich import print, inspect

def main():
    print("[purple]Criando a conta...[/]")
    cc = ContaBancaria(123, "Gustavo", 1000)

    print("[purple]Realizando deposito[/]")
    cc.depositar(500)

    print("[purple]Realizando saque[/]")
    cc.sacar(200)

    cc.nome = "Manoel"

    print(cc)

    inspect(cc, private=True, methods=True)


if __name__ == "__main__":
    main()
