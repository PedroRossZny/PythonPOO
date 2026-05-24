from cafe import Cafe
from cha import Cha
from leite import Leite

def main():
    b1 = Cafe()
    b2 = Cha()
    b3 = Leite()

    b1.preparar()
    print()
    b2.preparar()
    print()
    b3.preparar()

if __name__ == "__main__":
    main()