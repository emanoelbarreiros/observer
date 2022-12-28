from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self):
        pass

class ObservadorArquivo(ABC):
    @abstractmethod
    def notificar(self, tipo_evento, arquivo):
        pass