from abc import ABC, abstractmethod
from random import randint, choice
from rich import print

class Personagem(ABC):
    def __init__(self, nome = "", vida = 0, golpes = None):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        golpe = choice(self.golpes)
        ataque = randint(1, forca)
        dano = alvo.vida - ataque
        print(f"[green]{self.nome}[/]({self.vida}) atacou [red bold]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de forca {forca}")
        print(f"[blue]{alvo.nome}[/] {self.receber_dano(ataque)}")
        alvo.vida -= ataque

    def receber_dano(self, dano):
        return f"recebeu [red]dano de {dano}[/]!"

    @abstractmethod
    def curar(self):
        pass