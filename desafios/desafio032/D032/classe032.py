from hashlib import sha256
from rich import print

class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id:int, nome:str | None=None, saldo:float = 0, chave=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo
        if chave == None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f"[blue]Conta [yellow]{self._id}[blue] criada com sucesso. Saldo atual de [green]R${self.__saldo:.2f}[/]")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome:str | None=None):
        senha = self.pede_senha()
        if self.validar_senha(senha):
            self._titular = nome
            print(f"[blue]Nome do titular agora e [yellow]{self._titular}")
        else:
            print("[red]Senha nao autorizada.[/]")

    def depositar(self, valor):
        self.__saldo += valor
        print(f"[yellow]Deposito de [green]R${valor:.2f}[yellow] autorizado na conta [purple]{self._id}[/]")

    def sacar(self, valor:float, chave:str | None=None):
        if chave != None:
            if self.validar_senha(chave):
                self.__saldo -= valor
                print(f"[yellow]Saque de [green]R${valor:.2f}[yellow] autorizado na conta [purple]{self._id}[/]")
            else:
                print("[red]Senha nao confere. Saque nao autorizado![/]")
        else:
            chave = self.pede_senha()
            if self.validar_senha(chave):
                self.__saldo -= valor
                print(f"[yellow]Saque de [green]R${valor:.2f}[yellow] autorizado na conta [purple]{self._id}[/]")
            else:
                print("[red]Senha nao confere. Saque nao autorizado![/]")

    def pede_senha(self) -> str:
        return str(input("Senha: "))

    def validar_senha(self, chave:str) -> bool:
        chave = sha256(chave.encode('utf-8')).hexdigest()
        if chave == self.__hash:
            return True
        else:
            return False

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:.2f}."
