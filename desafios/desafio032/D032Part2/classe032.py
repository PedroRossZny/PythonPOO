from hashlib import sha256

class ContaBancaria:
    """
Cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id # protegido (#)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        if chave is None:
            chave = self.pede_senha()
        self._hash = sha256(chave.encode()).hexdigest()
        print(f"Conta {self._id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}")

    def pede_senha(self) -> str:
        from pwinput import pwinput

        while True:
            senha = str(pwinput("Senha: ")).strip()
            if len(senha) >= 6:
                break
        return senha

    def validar_senha(self, chave:str) -> bool:
        usuario = sha256(chave.encode()).hexdigest()
        if usuario == self._hash:
            return True
        else:
            return False

    def __str__(self):
        return f"A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de saldo"
        # return f"Estado atual da conta: {self.__dict}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de RS{valor:,.2f} autorizado na conta {self._id}")

    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)

        if chave is None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f"Saque NEGADO de R${valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE")
            else:
                self.__saldo -= valor
                print(f"Saque de RS{valor:,.2f} autorizado na conta {self._id}")
        else:
            print(f"Senha nao confere. Saque nao autorizado!")

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, novonome:str = None):
        chave = self.pede_senha()

        if self.validar_senha(chave):
            if len(novonome) >= 5:
                self._titular = novonome
            else:
                print("Senha nao confere. Nao posso alterar o nome")
