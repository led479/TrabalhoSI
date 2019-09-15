from .gerador_de_matriz import GeradorDeMatriz

class Estado:
    def __init__(self):
        self.matriz = GeradorDeMatriz().gera_matriz_aleatoria()

        # TODO Adicionar algoritmo para custo
        self.custo = 0

        # TODO Adicionar algoritmo para heurística
        self.heuristica = None

    def indice_do_vazio(self):
        for i in range(len(self.matriz)):
              for j in range(len(self.matriz[i])):
                  if(self.matriz[i][j] == None):
                      return [i, j]

    