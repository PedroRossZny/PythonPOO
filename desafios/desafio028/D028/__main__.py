from classes028 import Termostato
from rich import print, inspect

def main():
    t = Termostato()
    t.temperatura = 25
    inspect(t, private=True, methods=True)
    print(f"[blue]A temperatura atual e {t.ftemperatura}[/]")

if __name__ == "__main__":
    main()
