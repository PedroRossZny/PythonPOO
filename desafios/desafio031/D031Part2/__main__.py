from classe031 import Retangulo

def main():
    r = Retangulo()
    try:
        r.base = 12
        r.altura = 7
        r.medidas = (8, 12)

    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
