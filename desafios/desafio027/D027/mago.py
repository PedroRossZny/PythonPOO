from personagem import *
from random import randint
from rich import print

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Meteoro", "Rajada de Luz"]

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] fez uma magia de cura e [green]recuperou {cura} pontos[/] de vida.")