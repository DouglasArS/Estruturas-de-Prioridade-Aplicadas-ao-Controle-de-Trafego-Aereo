from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from HeapBinaria import FP_HeapBinaria

class UserInterface:
    def __init__(self):
        self.initializeUi()

    def initializeUi(self):
        self.app = QtWidgets.QApplication([])

        self.fp = FP_HeapBinaria(10000)

        self.ui = loadUi("./aeroportoed2.ui")
        
        self.ui.AviaoPouso.setText("Nenhum Avião Solicitou Pouso.")

        self.ui.Inserir.clicked.connect(self.inserir)
        self.ui.Remover.clicked.connect(self.remover)

        self.ui.show()
        self.app.exec()
    
    def inserir(self):
        nome = self.ui.LerNome.text()
        combustivel = self.ui.LerCombustivel.text()

        self.fp.inserir(nome, combustivel)

        self.ui.AviaoPouso.setText("Nome: " + self.fp.dados[0].nome + " - " \
            + "Nivel de Combustível: " + self.fp.dados[0].prioridade + "%")
        
        self.ui.LerNome.clear()
        self.ui.LerCombustivel.clear()
        
        self.fp.mostrar()
        print()
    
    def remover(self):
        self.fp.remover()

        if self.fp.vazia():
            self.ui.AviaoPouso.setText("Nenhum Avião Solicitou Pouso.")
        else:
            self.ui.AviaoPouso.setText("Nome: " + self.fp.dados[0].nome + " - " \
            + "Nivel de Combustível: " + self.fp.dados[0].prioridade + "%")

        self.fp.mostrar()
        print()


if __name__ == "__main__":
    ui = UserInterface()