from Objeto import Objeto
from math import floor, ceil

class HeapBinaria:
    def __init__(self, tamanho_maximo) -> None:
        self.quantidade = 0
        self.tamanho_maximo = tamanho_maximo
        self.dados = []

    def tamanho(self):
        return self.quantidade

    def vazia(self):
        return self.quantidade == 0
    
    def cheia(self):
        return self.quantidade == self.tamanho_maximo

    def __subir(self):
        filho = self.quantidade
        pai = (filho - 1) // 2
        temp = Objeto()

        while filho > 0 and self.dados[pai].prioridade <= self.dados[filho].prioridade:
            temp = self.dados[filho]
            self.dados[filho] = self.dados[pai]
            self.dados[pai] = temp

            filho = pai
            pai = (pai - 1) // 2

    def inserir(self, nome, prioridade):
        # Verificar se a Heap está cheia
        if(self.quantidade == self.tamanho_maximo):
            return False
        
        novo_dado = Objeto(nome, prioridade)
        self.dados.insert(self.quantidade, novo_dado)
        self.__subir()
        self.quantidade += 1

    def mostrar(self):
        for i in self.dados:
            print(i)

if __name__ == "__main__":
    filap = HeapBinaria(10)

    print("\n === Primeira Inserção ====")
    filap.inserir("A152", 28)
    filap.inserir("AF15", 60)
    filap.mostrar()

    print("\n === Segunda Inserção ====")
    filap.inserir("A250", 70)
    filap.inserir("B350", 39)
    filap.inserir("0G15", 95)
    filap.mostrar()

    print("\n === Terceira Inserção ====")
    filap.inserir("F48", 33)
    filap.inserir("C987", 78)
    filap.inserir("X58", 66)
    filap.mostrar()