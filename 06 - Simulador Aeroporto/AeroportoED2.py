from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from FP_HeapFibonacci import FP_HeapFibonacci
import sys
sys.path.append("../Analise-das-estruturas-de-prioridades/06 - Simulador Aeroporto/")

class UserInterface:
    def __init__(self):
        self.initializeUi()

    def initializeUi(self):
        self.app = QtWidgets.QApplication([])

        self.fp = FP_HeapFibonacci()

        self.ui = loadUi("./06 - Simulador Aeroporto/aeroportoed2.ui")
        
        self.ui.AviaoPouso.setText("Nenhum Avião Solicitou Pouso.")

        self.ui.Inserir.clicked.connect(self.inserir)
        self.ui.Remover.clicked.connect(self.remover)

        self.ui.show()
        self.app.exec()
    
    def inserir(self):
        nome = self.ui.LerNome.text()
        combustivel = self.ui.LerCombustivel.text()

        self.fp.inserir(nome, combustivel)

        self.ui.AviaoPouso.setText("Nome: " + self.fp.mini.nome + " - " \
            + "Nivel de Combustível: " + self.fp.mini.prioridade + "%")
        
        self.ui.LerNome.clear()
        self.ui.LerCombustivel.clear()
        
        self.fp.mostrar()
        print()
    
    def remover(self):
        self.fp.remover()

        if self.fp.vazia():
            self.ui.AviaoPouso.setText("Nenhum Avião Solicitou Pouso.")
        else:
            self.ui.AviaoPouso.setText("Nome: " + self.fp.mini.nome + " - " \
            + "Nivel de Combustível: " + self.fp.mini.prioridade + "%")

        self.fp.mostrar()
        print()


if __name__ == "__main__":
    ui = UserInterface()