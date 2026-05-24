from personagem import *
from random import randint
from rich import print

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Pulo Giratorio", "Golpe de Machado"]

    def curar(self):
        cura = randint(1, 100)
        self.vida += cura
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida.")