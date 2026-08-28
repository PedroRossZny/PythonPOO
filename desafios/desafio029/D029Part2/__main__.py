from classes029 import Diario
from rich import print

def main():
     meudiario = Diario()
     meudiario.escrever("Essa e a primeira mensagem")
     meudiario.escrever("Estou aprendendo Python")
     try:
         meudiario.ler('Teste123')
     except Exception as e:
         print(f"[red]ERRO: {e}")

     # inspect(meudiario, private = True)

if __name__ == '__main__':
    main()
