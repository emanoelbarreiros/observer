from funcionamento.interfaces import ObservadorArquivo

class EventManager:

    def __init__(self, *operacoes):
        self.escutadores = {}
        for operacao in operacoes:
            self.escutadores[operacao] = []

    def inscrever(self, tipo_evento, escutador):
        escutadores = self.escutadores[tipo_evento]
        escutadores.append(escutador)

    def desinscrever(self, tipo_evento, escutador):
        escutadores = self.escutadores[tipo_evento]
        escutadores.remove(escutador)

    def notificar(self, tipo_evento, arquivo):
        escutadores = self.escutadores[tipo_evento]
        for escutador in escutadores:
            escutador.notificar(tipo_evento, arquivo)
