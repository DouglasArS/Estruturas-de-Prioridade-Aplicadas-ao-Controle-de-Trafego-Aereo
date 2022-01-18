from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from FP_HeapFibonacci import FP_HeapFibonacci
import sys
sys.path.append("../Analise-das-estruturas-de-prioridades/05 - Simulador Aeroporto/")

class UserInterface:
    def __init__(self):
        self.initializeUi()

    def initializeUi(self):
        # Criando a Janela.
        self.app = QtWidgets.QApplication([])

        # Criando a Fila de Prioridade.
        self.fp = FP_HeapFibonacci()

        # Carregando a interface do usuário.
        self.ui = loadUi("./05 - Simulador Aeroporto/aeroportoed2.ui")
        
        # Estabelecendo o aviso de fila vazia.
        self.ui.AviaoPouso.setText("Nenhum Avião Solicitou Pouso.")

        # Estabelecendo a ação do botão inserir.
        self.ui.Inserir.clicked.connect(self.inserir)

        # Estabelecendo a ação do botão remover.
        self.ui.Remover.clicked.connect(self.remover)

        # Executando a tela e começando o loop da janela aberta.
        self.ui.show()
        self.app.exec()
    
    def inserir(self):
        # Obtendo o nome e o nível de combustível do usuário.
        nome = self.ui.LerNome.text()
        combustivel = self.ui.LerCombustivel.text()

        # Realizando a operação de inserir dentro da fila de prioridade 
        # com as informações obtidas anteriormente.
        self.fp.inserir(nome, combustivel)

        # Mostrando o avião habilitado para pouso.
        self.ui.AviaoPouso.setText("Nome: " + self.fp.mini.nome + " - " \
            + "Nivel de Combustível: " + self.fp.mini.prioridade + "%")
        
        # Limpando as caixas de entrada do usuário.
        self.ui.LerNome.clear()
        self.ui.LerCombustivel.clear()
        
        # Printando no terminal a fila de prioridade.
        self.fp.mostrar()
        print()
    
    def remover(self):
        # Realizando a operação de remover dentro da fila de prioridade.
        self.fp.remover()

        # Verificando a situação da fila de prioridade e atualizando o
        # label que mostra avião habilitado para pouso.
        if self.fp.vazia():
            self.ui.AviaoPouso.setText("Nenhum Avião Solicitou Pouso.")
        else:
            self.ui.AviaoPouso.setText("Nome: " + self.fp.mini.nome + " - " \
            + "Nivel de Combustível: " + self.fp.mini.prioridade + "%")

        # Printando no terminal as fila de prioridade.
        self.fp.mostrar()
        print()


if __name__ == "__main__":
    # Inicializando a interface gráfica, criando o objeto UserInterface.
    ui = UserInterface()