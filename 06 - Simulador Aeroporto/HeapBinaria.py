from Objeto import Objeto
import time

class FP_HeapBinaria:
    def __init__(self, tamanho_maximo) -> None:
        self.quantidade = 0
        self.tamanho_maximo = tamanho_maximo
        self.dados = self.dados = [None] * tamanho_maximo

    def tamanho(self):
        return self.quantidade

    def vazia(self):
        # Verificando se quantidade é igual a 0.
        return self.quantidade == 0
    
    def cheia(self):
        # Verificando se quantidade é igual ao tamanho máximo.
        return self.quantidade == self.tamanho_maximo

    def __subir(self, filho):
        # Calculando a posição do pai.
        pai =(filho - 1) // 2

        # Criando um objeto temporário que auxiliará nas trocas.
        temp = Objeto()

        # Realizando a subida do elemento.
        while filho > 0 and self.dados[pai].prioridade >= self.dados[filho].prioridade:

            # Efetuando a troca entre os elementos pai e filho.
            temp = self.dados[filho]
            self.dados[filho] = self.dados[pai]
            self.dados[pai] = temp

            # Atualizando o pai e o filho.
            filho = pai
            pai = (pai - 1) // 2

    def inserir(self, nome, prioridade):
        # Verificar se a Heap está cheia.
        if self.cheia():
            print("Fila Cheia.")
            return False
        
        # Criando o elemento (objeto) a ser inserido.
        novo_dado = Objeto(nome, prioridade)

        # Inserindo o elemento na ultima posição da Heap.
        self.dados[self.quantidade] = novo_dado

        # Subindo o elemento para posição correta.
        self.__subir(filho = self.quantidade)

        # Incrementando em uma unidade o valor quantidade.
        self.quantidade += 1

        return True

    def __descer(self, pai):
        # Criando um objeto temporário que auxiliará nas trocas.
        temp = Objeto()
        
        # Calculando a posiçãodo filho.
        filho = 2 * pai + 1

        # Realizando a descida do elemento.
        while filho < self.quantidade:

            # Verificando se o pai tem 2 filhos.
            if filho < (self.quantidade - 1):

                # Verificando qual filho tem maior prioridade.
                if self.dados[filho].prioridade > self.dados[filho + 1].prioridade:
                    # Caso o segundo filho tenha maior prioridade, será ele o escolhido.
                    filho += 1

            # Verificando se pai ainda tem maior prioridade que o filho.
            if self.dados[pai].prioridade <= self.dados[filho].prioridade:
                break

            # Efetuando a troca entre os elementos pai e filho.
            temp = self.dados[pai]
            self.dados[pai] = self.dados[filho]
            self.dados[filho] = temp

            # Atualizando o pai e o filho.
            pai = filho
            filho = 2 * pai + 1
    
    def remover(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Decrementando em uma unidade o valor quantidade.
        self.quantidade -= 1

        # Colocando o ultimo elemento no topo (no lugar do elemento removido).
        self.dados[0] = self.dados[self.quantidade]

        # Descendo o elemento que foi inserido no topo para a sua posição correta.
        self.__descer(pai = 0)

        return True

    def consultar(self):
        # Verificando se a fila está vazia.
        if self.vazia():
            print("Fila Vazia.")
            return False

        # Mostrando o elemento do topo da fila (maior prioridade).
        print(self.dados[0])

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
    
    fp = FP_HeapBinaria(100000)

    fp.inserir("X14", 12)
    fp.mostrar()

    print()

    fp.inserir("G1F4", 25)
    fp.mostrar()
    print()

    fp.inserir("Xda", 30)
    fp.mostrar()

    print()

    fp.inserir("AAA", 10)
    fp.mostrar()

    print(fp.dados[0])

      