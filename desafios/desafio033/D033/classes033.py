from abc import ABC, abstractmethod
from datetime import date

ano_atual = date.today().year

class Pessoa(ABC):
    def __init__(self):
        self._nome = None
        self._nascimento = None

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nasc:int):
        if nasc > ano_atual or nasc < (ano_atual - 100):
            raise ValueError(f"Ano {nasc} e invalido")
        else:
            self._nascimento = nasc

    @property
    def idade(self):
        return ano_atual - self._nascimento

    @idade.setter
    def idade(self, idade):
        raise PermissionError("Voce nao pode alterar a idade. Mude o ano de nascimento")

class Aluno(Pessoa):
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__()
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O Curso {curso} nao esta na lista de cursos oficiais.")
        self._curso = curso
        self._nome = nome
        self._nascimento = nasc

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso:str):
        if curso not in self.cursos_oficiais:
            raise ValueError(f"O Curso {curso} nao esta na lista de cursos oficiais.")
        else:
            self._curso = curso

    def add_curso(self, curso:str):
        self.cursos_oficiais.append(curso)