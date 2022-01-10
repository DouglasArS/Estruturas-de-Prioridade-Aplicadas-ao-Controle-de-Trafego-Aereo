from Objeto import Objeto
from math import floor, ceil

class FP_VetorOrdenado:
    def __init__(self, tamanho_maximo) -> None:
        self.quantidade = 0
        self.tamanho_maximo = tamanho_maximo
        self.dados = [None] * tamanho_maximo

    def tamanho(self):
        return self.quantidade

    def vazia(self):
        return self.quantidade == 0
    
    def cheia(self):
        return self.quantidade == self.tamanho_maximo

    def inserir(self, nome, prioridade) -> None:
        i = self.quantidade - 1
        while(i >= 0 and self.dados[i].prioridade <= prioridade):
            self.dados[i + 1] = self.dados[i]
            i -= 1
        
        novo_dado = Objeto(nome, prioridade)
        self.dados[i + 1] = novo_dado
        self.quantidade += 1

    def remover(self):
        if self.quantidade == 0:
            return False
        
        self.quantidade -= 1
        return True

    def consulta(self):
        if self.quantidade == 0:
            print("Lista Vazia.")
        else:
            print(self.dados[self.quantidade - 1])

    def mostrar(self):
        i = self.quantidade - 1
        while(i >= 0):
            print(self.dados[i])
            i -= 1

if __name__ == "__main__":
    filap = FP_VetorOrdenado(20)

    print("\n ==== Primeira Inserção ====")
    filap.inserir("A152", 28)
    filap.mostrar()

    print("\n ==== Segunda Inserção ====")
    filap.inserir("AF15", 60)
    filap.mostrar()

    print("\n==== Terceira Inserção ====")
    filap.inserir("A250", 30)
    filap.mostrar()

    print("\n==== Quarta Inserção ====")
    filap.inserir("B100", 12)
    filap.inserir("F850", 55)
    filap.inserir("Z496", 10)
    filap.inserir("X150", 94)
    filap.mostrar()

    print("\n==== Primeira Remoção ====")
    filap.remover()
    filap.remover()
    filap.mostrar()

    print("\n==== Primeira Consulta ====")
    filap.consulta()