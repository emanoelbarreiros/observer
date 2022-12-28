from typing import Type
from .interfaces import Observador

class Som:
    def __init__(self):
        self.barulho = False
        self.descansando = []

    def adicionaPessoa(self, pessoa: Type[Observador]):
        self.descansando.append(pessoa)

    def estado_som(self):
        return self.barulho

    def tocar(self):
        self.barulho = True
        for pessoa in self.descansando:
            pessoa.atualizar()

        self.descansando = []
