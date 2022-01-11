from Objeto import Objeto
import time

class FP_VetorDesordenado:
    def __init__(self, tamanho_maximo) -> None:
        self.quantidade = 0
        self.tamanho_maximo = tamanho_maximo
        self.dados = [None] * tamanho_maximo

    def tamanho(self):
        return self.quantidade

    def vazia(self):
        # Verificando se quantidade é igual a 0.
        return self.quantidade == 0
    
    def cheia(self):
        # Verificando se quantidade é igual ao tamanho máximo.
        return self.quantidade == self.tamanho_maximo

    def inserir(self, nome, prioridade):
        # Verificando se a fila está cheia.
        if self.cheia():
            print("Fila Cheia.")
            return False

        # Criando o elemento (objeto) a ser inserido.
        novo_dado = Objeto(nome, prioridade)

        # Inserindo o novo elemento na última posição.
        self.dados[self.quantidade] = novo_dado

        # Incrementando em uma unidade o valor quantidade.
        self.quantidade += 1

        return True

    def remover(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Procurando o elemento de menor prioridade.
        menor = self.dados[0]
        indice = 0

        for i in range(1, self.quantidade):
            if menor.prioridade > self.dados[i].prioridade:
                menor = self.dados[i]
                indice = i

        # Preenchendo o elemento removido com seus sucessores.
        for i in range(indice, self.quantidade - 1):
            self.dados[i] = self.dados[i + 1]

        # Decrementando em uma unidade o valor quantidade.
        self.quantidade -= 1

        return True

    def consultar(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Procurando o elemento de menor prioridade.
        menor = self.dados[0]
        indice = 0

        for i in range(1, self.quantidade):
            if menor.prioridade > self.dados[i].prioridade:
                menor = self.dados[i]
                indice = i
        
        # Mostrando o elemento de menor prioridade
        print(self.dados[indice])
    
        return True

    def mostrar(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False
        
        # Mostrando todos os elementos conforme os níveis do heap.
        for i in range(self.quantidade):           
            print(self.dados[i])

        return True


if __name__ == "__main__":
    
    total_de_interacao = 10
    tempo_acumulado = 0

    for i in range(0, total_de_interacao):
        tempo_inicial = time.time()

        fp = FP_VetorDesordenado(100000)

        for j in range(1, 10000):
            fp.inserir(nome = "A" + str(j), prioridade = j)            

        for j in range(0, 5000):
            fp.remover()
            fp.consultar()

        for j in range(1, 10000):
            fp.inserir(nome = "B" + str(j), prioridade = j)
            fp.consultar()

        for j in range(0, 5000):
            fp.remover()
            fp.consultar()

        for j in range(0, 10000):
            fp.remover()

        tempo_acumulado += (time.time() - tempo_inicial)

    print("Tempo = {:.2f}", tempo_acumulado / total_de_interacao)