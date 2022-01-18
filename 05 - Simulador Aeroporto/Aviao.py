class Aviao:
    def __init__(self) -> None:
        self.nome = None
        self.prioridade = -1
        self.pai = None
        self.filho = None
        self.esquerda = None
        self.direita = None
        self.grau = -1
    
    def __repr__(self):
        rep = "Nome: " + str(self.nome) + " | " + "Nível de Combustível: " + str(self.prioridade)        
        return rep

    def __str__(self) -> str:
        return self.__repr__()