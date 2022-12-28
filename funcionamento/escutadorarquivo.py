from funcionamento.interfaces import ObservadorArquivo


class EscutadorAbrir(ObservadorArquivo):

    def notificar(self, tipo_evento, arquivo):
        print(tipo_evento, "o arquivo foi aberto: ", arquivo)

class EscutadorSalvar(ObservadorArquivo):

    def notificar(self, tipo_evento, arquivo):
        for linha in arquivo:
            print(linha)

class EscutadorArquivo(ObservadorArquivo):
    def notificar(self, tipo_evento, arquivo):
        if tipo_evento == "abrir":
            print(tipo_evento, "o arquivo foi aberto: ", arquivo)
        elif tipo_evento == "salvar":
            for linha in arquivo:
                print(linha)