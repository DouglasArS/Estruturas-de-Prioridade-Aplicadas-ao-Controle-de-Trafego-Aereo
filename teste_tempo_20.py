if __name__ == "__main__":
    
    total_de_interacao = 10
    tempo_acumulado = 0

    for i in range(0, total_de_interacao):
        tempo_inicial = time.time()

        fp = FP_VetorDesordenado(100000)

        for j in range(1, 10):
            fp.inserir(nome = "A" + str(j), prioridade = j)            

        for j in range(0, 5):
            fp.remover()
            fp.consultar()

        for j in range(1, 10):
            fp.inserir(nome = "B" + str(j), prioridade = j)
            fp.consultar()

        for j in range(0, 5):
            fp.remover()
            fp.consultar()

        for j in range(0, 10):
            fp.remover()

        tempo_acumulado += (time.time() - tempo_inicial)

    print("Tempo = {:.2f}", tempo_acumulado / total_de_interacao)