import random

class GeradorDeMatriz:
    def __init__(self):
        self.numeros_disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, None]
        random.shuffle(self.numeros_disponiveis)

    # Retorna uma matriz com 8 números entre 1 e 8, e um espaço vazio (None)
    # Ex:   [   [5, 3, 4],
    #           [2, None, 7],
    #           [1, 6, 8]
    #       ]
    def gera_matriz_aleatoria(self):
        m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(m)):
            for j in range(len(m[i])):
                m[i][j] = self.numeros_disponiveis.pop()

        return m