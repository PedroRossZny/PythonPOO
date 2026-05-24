from rich import print, inspect
from circulo import Circulo
from quadrado import Quadrado

def main():
    q1 = Quadrado(12)
    c1 = Circulo(20)

    print(f"Perimetro do [yellow]quadrado[/] = {q1.perimetro():.1f}")
    print(f"Area do [yellow]quadrado[/] = {q1.area():.1f}\n")
    print(f"Perimetro do [yellow]circulo[/] = {c1.perimetro():.1f}")
    print(f"Area do [yellow]circulo[/] = {c1.area():.1f}")

if __name__ == "__main__":
    main()