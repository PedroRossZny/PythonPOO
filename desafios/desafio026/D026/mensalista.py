from funcionario import *

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_sal(self):
        self.salario = self.sal_bruto - ((self.inss / 100) * self.sal_bruto)