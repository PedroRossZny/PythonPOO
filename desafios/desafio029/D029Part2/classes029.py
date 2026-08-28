from rich import print

class Diario:

    def __init__(self, senhamestra = 'CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError('Senha invalida! Voce nao pode ler meu diario!')
        else:
            print(f"[green]Diario LIBERADO![/]")
            for segredo in self.__segredos:
                print(f"- {segredo}")

    @property
    def senha(self):
        raise PermissionError('Ninguem tem permissao de ver a senha')

    @senha.setter
    def senha(self, novasenha):
        pass
