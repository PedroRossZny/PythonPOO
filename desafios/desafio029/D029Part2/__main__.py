from classes029 import Diario
from rich import print

def main():
    meudiario = Diario()
    meudiario.escrever("Essa e a primeira mensagem")
    meudiario.escrever("Estou aprendendo Python")
    try:
        meudiario.ler('CeV!@')
    except Exception as e:
        print(f"[red]ERRO: {e}")

    meudiario.senha = 'Pedro'
    meudiario.escrever("Nova mensagem depois de mudar a senha")
    try:
        meudiario.ler('Pedro')
    except Exception as e:
        print(f"[red]ERRO: {e}")

    # inspect(meudiario, private = True)

if __name__ == '__main__':
    main()
