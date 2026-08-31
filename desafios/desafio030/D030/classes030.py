from hashlib import sha256
from rich import print

class Credencial:
    def __init__(self):
        self.__hash = sha256("CeV!@".encode()).hexdigest()

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, senha):
        self.__hash = sha256(senha.encode()).hexdigest()

    def validar(self, chave):
        if sha256(chave.encode()).hexdigest() == self.senha:
            print(f"[green]Senha confere![/]")
            return True
        else:
            print(f"[red]Senha nao bate![/]")
            return False
