from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        favjogos = "\n:video_game: ".join(self.jogos)
        print(Panel(f"Nome real: [black on blue]{self.nome}[/]\n"
                        f"Jogos Favoritos:\n"
                        f":video_game: [blue]{favjogos}", title=f"Jogador <{self.nick}>", width=45))

j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Fortnite")
j1.add_favoritos("God of War")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.ficha()

j2 = Gamer("Olivia Souza", "peach_raivosa")
j2.add_favoritos("Call of Duty")
j2.add_favoritos("Mario Bros")
j2.ficha()