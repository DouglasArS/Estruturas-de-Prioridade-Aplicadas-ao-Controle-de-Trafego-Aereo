if __name__ == "__main__":
    fp = FP_VetorDesordenado(20)

    print("\n\n === Primeira Inserção ====")
    fp.inserir("A152", 28)
    fp.inserir("AF15", 60)
    fp.mostrar()

    print("\n === Primeira Consulta ====")
    fp.consultar()

    print("\n === Primeira Remoção ====")
    fp.remover()
    fp.mostrar()


    print("\n\n\n === Segunda Inserção ====")
    fp.inserir("A250", 70)
    fp.inserir("B350", 39)
    fp.inserir("0G15", 95)
    fp.mostrar()

    print("\n === Segunda Consulta ====")
    fp.consultar()

    print("\n === Segunda Remoção ====")
    fp.remover()
    fp.mostrar()


    print("\n\n\n === Terceira Inserção ====")
    fp.inserir("F48", 33)
    fp.mostrar()

    print("\n === Terceira Consulta ====")
    fp.consultar()

    print("\n === Terceira Remoção ====")
    fp.remover()
    fp.mostrar()


    print("\n\n\n === Quarta Inserção ====")
    fp.inserir("C987", 78)
    fp.inserir("X58", 66)
    fp.mostrar()

    print("\n === Quarta Consulta ====")
    fp.consultar()

    print("\n === Quarta Remoção ====")
    fp.remover()
    fp.mostrar()


    print("\n\n\n === Quinta Inserção ====")
    fp.inserir("F14", 94)
    fp.inserir("L896", 100)
    fp.mostrar()

    print("\n === Quinta Consulta ====")
    fp.consultar()

    print("\n === Quinta Remoção ====")
    fp.remover()
    fp.mostrar()


    print("\n\n\n === Sexta Inserção ====")
    fp.inserir("F14", 45)
    fp.inserir("L896", 110)
    fp.mostrar()

    print("\n === Sexta Remoção ====")
    fp.remover()
    fp.mostrar()

    print("\n === Sexta Consulta ====")
    fp.consultar()

    print("\n")