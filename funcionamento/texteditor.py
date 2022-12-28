"""
- implementar uma subclasse da classe Editor chamada TextEditor;
- aplicar o método insertLine, que recebe os parâmetros lineNumber e text;
- inserir o texto na ordem correspondente a lineNumber e deslocar as 
linhas posteriores se necessário;
- aplicar o método removeLine, que recebe lineNumber como parâmetro, 
deleta o texto da linha correspondente e desloca as linhas posteriores se necessário;
- instanciar um TextEditor e disparar o evento “open”;
- receber as linhas de texto, que serão inseridas no objeto textEditor, 
do usuário até que ele envie o texto “EOF”, que não deve ser inserido no objeto textEditor;
- por fim, o textEditor deve disparar o evento “save” para que o conteúdo seja 
salvo no arquivo configurado e imprimir todo o conteúdo do arquivo na tela.
"""
from funcionamento.eventmanager import EventManager


class TextEditor:

    def __init__(self, nome_arquivo):
        self.arquivo = []
        self.nome_arquivo = nome_arquivo
        self.gerenciador_eventos = EventManager("abrir", "salvar")

    def inserir_linha(self, num_linha, texto):
        self.arquivo.insert(num_linha, texto)

    def remover_linha(self, num_linha):
        self.arquivo.pop(num_linha)

    def abrir(self):
        self.gerenciador_eventos.notificar("abrir", self.nome_arquivo)

    def salvar(self):
        self.gerenciador_eventos.notificar("salvar", self.arquivo)