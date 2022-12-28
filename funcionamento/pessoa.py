from .interfaces import Observador

class Pessoa(Observador):
    def __init__(self, nome):
        self.acordada = False
        self.nome = nome

    def esta_acordada(self):
        return self.acordada

    def atualizar(self):
        print(self.nome + " acordei")
        self.acordada = True