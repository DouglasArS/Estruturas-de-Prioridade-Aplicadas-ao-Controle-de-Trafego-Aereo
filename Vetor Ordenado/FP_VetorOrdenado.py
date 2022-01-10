from Objeto import Objeto

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

        # Criando o elemento (objeto) a ser inserido.
        novo_dado = Objeto(nome, prioridade)

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
        
        # Mostrando ultimo elemento do array (menor prioridade)
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
    fp = FP_VetorOrdenado(10)

    print("\n === Primeira Inserção ====")
    fp.inserir("A152", 28)
    fp.inserir("AF15", 60)
    fp.mostrar()

    print("\n === Segunda Inserção ====")
    fp.inserir("A250", 70)
    fp.inserir("B350", 39)
    fp.inserir("0G15", 95)
    fp.mostrar()

    print("\n === Terceira Inserção ====")
    fp.inserir("F48", 33)
    fp.inserir("C987", 78)
    fp.inserir("X58", 66)
    fp.inserir("X58", 94)
    fp.inserir("X58", 100)
    fp.mostrar()

    print("\n === Quarta Inserção ====")
    fp.inserir("X58", 94)
    fp.mostrar()

    print("\n === Terceira Inserção ====")
    fp.inserir("X58", 100)
    fp.mostrar()

    print("\n === Primeira Remoção ====")
    fp.remover()
    fp.mostrar()

    print("\n === Primeira Consulta ====")
    fp.consultar()

    print("\n === Segunda Remoção ====")
    fp.remover()
    fp.mostrar()

    print("\n === Segunda Consulta ====")
    fp.consultar()