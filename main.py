from funcionamento import EscutadorAbrir, EscutadorSalvar, EscutadorArquivo
from funcionamento.texteditor import TextEditor


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text_editor = TextEditor("arquivo_teste.txt")

    escutador = EscutadorArquivo()
    text_editor.gerenciador_eventos.inscrever("abrir", escutador)
    text_editor.gerenciador_eventos.inscrever("salvar", escutador)


    # escutador_abrir = EscutadorAbrir()
    # text_editor.gerenciador_eventos.inscrever("abrir", escutador_abrir)
    #
    # escutador_salvar = EscutadorSalvar()
    # text_editor.gerenciador_eventos.inscrever("salvar", escutador_salvar)

    text_editor.abrir()

    text_editor.inserir_linha(0, "primeira linha")
    text_editor.inserir_linha(1, "segunda linha")
    text_editor.inserir_linha(2, "terceira linha")

    text_editor.remover_linha(1)

    text_editor.salvar()