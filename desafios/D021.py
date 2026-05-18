from rich import print

class Caneta:
    def __init__(self,cor):
        self.cores = {"azul":"blue" , "vermelho":"red", "verde":"green"}
        self.cor = cor
        self.destampada = False

    def destampar(self):
        self.destampada = True

    def escrever(self, frase):
        if self.destampada:
            if self.cor == "azul":
                print(f"[{self.cores[self.cor]}]{frase}[/]", end="")
            elif self.cor == "vermelho":
                print(f"[{self.cores[self.cor]}]{frase}[/]", end="")
            elif self.cor == "verde":
                print(f"[{self.cores[self.cor]}]{frase}[/]", end="")
        else:
            print(f":no_entry_sign: A [{self.cores[self.cor]}]caneta[/] esta tampada! ", end="")

    def quebrar_linha(self, pulos):
        for p in range(pulos):
            print("")

c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Ola, tudo bem?")
c1.quebrar_linha(1)
c2.escrever("Ola, Gafanhoto!")
c1.quebrar_linha(1)
c3.escrever("Vamos exercitar!")