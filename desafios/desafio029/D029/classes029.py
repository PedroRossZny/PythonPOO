from rich import print

class Diario:
    def __init__(self,senhaMestra="CeV!@"):
        self.__segredos = []
        self.__senha = senhaMestra

    @property
    def senha(self):
        raise PermissionError('Ninguem tem permissao de ver a senha')

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha != self.__senha:
            raise PermissionError("Senha invalida! Voce nao pode ler meu diario!")
        else:
            print("[green bold]Diario LIBERADO![/]")
            for segredo in self.__segredos:
                print(f"[yellow bold]-[/] [blue]{segredo}[/]")
