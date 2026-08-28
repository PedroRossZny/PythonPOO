from classes028 import *

def main():
    t = Termostato()
    try:
        t.temperatura = 22.2
    except Exception as e:
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual e de {t.ftemperatura}")

if __name__ == '__main__':
    main()
