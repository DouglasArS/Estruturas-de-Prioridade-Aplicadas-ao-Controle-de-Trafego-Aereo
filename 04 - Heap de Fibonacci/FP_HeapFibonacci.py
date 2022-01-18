from Aviao import Aviao
import time, math

class FP_HeapFibonacci:
    def __init__(self) -> None:
        self.mini = None
        self.quantidade = 0

    def tamanho(self):
        return self.quantidade

    def vazia(self):
        # Verificando se quantidade é igual a 0.
        return self.quantidade == 0

    def inserir(self, nome, prioridade):
        # Criando o elemento (objeto) a ser inserido.
        novo_dado = Aviao()

        # Inserindo as informações do novo elemento.
        novo_dado.nome = nome
        novo_dado.prioridade = prioridade
        novo_dado.pai = None
        novo_dado.filho = None
        novo_dado.esquerda = novo_dado
        novo_dado.direita = novo_dado
        novo_dado.grau = 0

        if self.mini != None:
            self.mini.esquerda.direita = novo_dado
            novo_dado.direita = self.mini
            novo_dado.esquerda = self.mini.esquerda
            self.mini.esquerda = novo_dado

            if novo_dado.prioridade < self.mini.prioridade:
                self.mini = novo_dado
        else:
            self.mini = novo_dado

        self.quantidade += 1

    #  Vinculando os nós de heap no relacionamento pai-filho
    def __fibonnaci_link(self, no2, no1):
        no2.esquerda.direita = no2.direita
        no2.direita.esquerda = no2.esquerda

        if (no1.direita == no1):
            self.mini = no1

        no2.esquerda = no2
        no2.direita = no2
        no2.pai = no1

        if (no1.filho == None):
            no1.filho = no2

        no2.direita = no1.filho
        no2.esquerda = no1.filho.esquerda
        no1.filho.esquerda.direita = no2
        no1.filho.esquerda = no2

        if no2.prioridade < no1.filho.prioridade:
            no1.filho = no2

        no1.grau += 1
    
    # Consolidar a heap
    def __consolidar(self):
        temp2 = math.log2(self.quantidade)
        temp3 = int(temp2)

        array = [None] * (temp3 + 1)

        for i in range(temp3+1):
            array[i] = None

        no1 = self.mini
        no4 = no1

        while True:
            no4 = no4.direita
            temp1 = no1.grau

            while array[temp1] != None:
                no2 = array[temp1]

                if no1.prioridade > no2.prioridade:
                    no3 = no1
                    no1 = no2
                    no2 = no3

                if no2 == self.mini:
                    self.mini = no1

                self.__fibonnaci_link(no2, no1)

                if no1.direita == no1:
                    self.mini = no1

                array[temp1] = None
                temp1 += 1

            array[temp1] = no1
            no1 = no1.direita

            if no1 == self.mini:
                break

        self.mini = None

        for j in range(temp3 + 1):
            if array[j] != None:
                array[j].esquerda = array[j]
                array[j].direita = array[j]
                if (self.mini != None) :
                    self.mini.esquerda.direita = array[j]
                    array[j].direita = self.mini
                    array[j].esquerda = self.mini.esquerda
                    self.mini.esquerda = array[j]
                    if (array[j].prioridade < self.mini.prioridade):
                        self.mini = array[j]
                else:
                    self.mini = array[j]
                if self.mini == None:
                    self.mini = array[j]
                elif array[j].prioridade < self.mini.prioridade:
                    self.mini = array[j]
                    
    def remover(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False
        else:
            temp = self.mini
            no_atual = temp
            x = None

            if temp != None:
                if (temp.filho != None):
                    x = temp.filho

                    while(True):
                        no_atual = x.direita
                        self.mini.esquerda.direita = x
                        x.direita = self.mini
                        x.esquerda = self.mini.esquerda
                        self.mini.esquerda = x

                        if x.prioridade < self.mini.prioridade:
                            self.mini = x

                        x.pai = None
                        x = no_atual

                        if (no_atual == temp.filho):
                            break
        
                temp.esquerda.direita = temp.direita
                temp.direita.esquerda = temp.esquerda
                self.mini = temp.direita

                if temp == temp.direita and temp.filho == None:
                    self.mini = None
                else:
                    self.mini = temp.direita
                    self.__consolidar()

                self.quantidade -= 1

    def consultar(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Mostrando o elemento do topo da fila (maior prioridade).
        print(self.mini)
    
    def mostrar(self):
        if self.vazia():
            print("Fila Vazia.")
            return False
        else:
            no_atual = self.mini
            while(True):
                print(no_atual)
                no_atual = no_atual.direita
                if not(no_atual != self.mini and no_atual.direita != None):
                    break  
            True

if __name__ == "__main__":
    
    total_de_interacao = 10
    tempo_acumulado = 0

    for i in range(0, total_de_interacao):
        tempo_inicial = time.time()

        fp = FP_HeapFibonacci()

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