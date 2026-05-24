from funcionario import *

class FuncionarioHorista(Funcionario):
    def __init__(self, nome = "", valor_hora = 0, horas_trab = 0):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - ((self.inss / 100) * self.sal_bruto)