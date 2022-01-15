from Aviao import Aviao
import time

class FP_VetorOrdenado:
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

        # Criando variável para iterar no loop.
        i = self.quantidade - 1

        # Liberando a posição correta para inserir o novo elemento.
        while i >= 0 and self.dados[i].prioridade <= prioridade:
            self.dados[i + 1] = self.dados[i]
            i -= 1

        # Criando o elemento (Aviao) a ser inserido.
        novo_dado = Aviao(nome, prioridade)

        # Inserindo o novo elemento na posição correta.
        self.dados[i + 1] = novo_dado

        # Incrementando em uma unidade o valor quantidade.
        self.quantidade += 1

        return True

    def remover(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Decrementando em uma unidade o valor quantidade.
        self.quantidade -= 1

        return True

    def consultar(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False
        
        # Mostrando ultimo elemento do array (maiorr prioridade)
        print(self.dados[self.quantidade - 1])
    
        return True

    def mostrar(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Mostrando todos os elementos do array (do final para o inicio, de acordo com as prioridades).
        for i in range(self.quantidade - 1, 0, -1):           
            print(self.dados[i])

        return True
        

if __name__ == "__main__":
    
    total_de_interacao = 10
    tempo_acumulado = 0

    for i in range(0, total_de_interacao):
        tempo_inicial = time.time()

        fp = FP_VetorOrdenado(100000)

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
