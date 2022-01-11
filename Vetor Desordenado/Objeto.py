class Objeto():
    def __init__(self, nome = None, prioridade = None) -> None:
        self.nome = nome
        self.prioridade = prioridade

    def __repr__(self):
        rep = "Nome: " + str(self.nome) + " | " + "Nivel de Combustivel: " + str(self.prioridade) + "%"       
        return rep

    def __str__(self) -> str:
        return self.__repr__()