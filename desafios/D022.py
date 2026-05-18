from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self):
        self.canais = "[on yellow] 1 [/] 2  3  4  5 "
        self.volumeTotal = "[on blue]  [on white]   [/]"
        self.canal = 1
        self.volume = 2

        while True:
            tv = Panel(":no_entry_sign: [red]A TV esta desligada[/]", title="[ TV ]", width=40)
            liga_desliga = False
            print(tv)
            botoes = str(input("< CH1 >   - VOL1 + "))
            print(f"{"\n"*8}")
            if botoes == "@" and not liga_desliga:
                liga_desliga = True
                while liga_desliga:
                    tv = Panel(f"CANAL = {self.canais}\n"
                               f"VOLUME = {self.volumeTotal}", title="[ TV ]", width=40)
                    print(tv)
                    botoes = str(input("< CH1 >   - VOL1 + "))
                    print(f"{"\n"*8}")
                    while botoes == "0":
                        print("\n[red]Desligue a TV para sair do programa[/]\n")
                        tv = Panel(f"CANAL = {self.canais}\n"
                                   f"VOLUME = {self.volumeTotal}", title="[ TV ]", width=40)
                        print(tv)
                        botoes = str(input("< CH1 >   - VOL1 + "))
                        print(f"{"\n"*8}")
                    if botoes == "+" or botoes == "-":
                        if botoes == "+":
                            self.volume += 1
                        else:
                            self.volume -= 1
                        if self.volume >= 5:
                            self.volumeTotal = "[on blue]     [/]"
                            self.volume = 5
                        elif self.volume <= 1:
                            self.volumeTotal = "[on blue] [on white]    [/]"
                            self.volume = 1
                        else:
                            if self.volume == 2:
                                self.volumeTotal = "[on blue]  [on white]   [/]"
                            elif self.volume == 3:
                                self.volumeTotal = "[on blue]   [on white]  [/]"
                            elif self.volume == 4:
                                self.volumeTotal = "[on blue]    [on white] [/]"
                    elif botoes == "<" or botoes == ">":
                        if botoes == ">":
                            self.canal += 1
                        else:
                            self.canal -= 1
                        if self.canal > 5:
                            self.canais = "[on yellow] 1 [/] 2  3  4  5 "
                            self.canal = 1
                        elif self.canal < 1:
                            self.canais = " 1  2  3  4 [on yellow] 5 [/]"
                            self.canal = 5
                        else:
                            if self.canal == 1:
                                self.canais = "[on yellow] 1 [/] 2  3  4  5 "
                            elif self.canal == 2:
                                self.canais = " 1 [on yellow] 2 [/] 3  4  5 "
                            elif self.canal == 3:
                                self.canais = " 1  2 [on yellow] 3 [/] 4  5 "
                            elif self.canal == 4:
                                self.canais = " 1  2  3 [on yellow] 4 [/] 5 "
                            elif self.canal == 5:
                                self.canais = " 1  2  3  4 [on yellow] 5 [/]"
                    elif botoes == "@":
                        break
                    else:
                        print(Panel.fit("[bold red]--Botao invalido--\n"
                                        "[yellow]@ =[green] liga[yellow]/[red]desliga\n"
                                        "[yellow]+/- =[green] volume+[yellow]/[red]volume-\n"
                                        "[yellow]</> =[blue] canal<[yellow]/[blue]canal>[/]\n"
                                        "[yellow]0 = [red]SAIR DO PROGRAMA[/]", title=" ERRO ", style="red"))
            elif botoes == "0":
                break
            else:
                print(Panel.fit("[bold red]--Botao invalido--\n"
                      "[yellow]@ =[green] liga[yellow]/[red]desliga\n"
                      "[yellow]+/- =[green] volume+[yellow]/[red]volume-\n"
                      "[yellow]</> =[blue] canal<[yellow]/[blue]canal>[/]\n"
                                "[yellow]0 = [red]SAIR DO PROGRAMA[/]", title=" ERRO ", style="red"))

tv1 = ControleRemoto()