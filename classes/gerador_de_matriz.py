from random import randrange

class GeradorDeMatriz:
    def __init__(self):
        self.numeros_ja_gerados = []

    def numero_entre_1_e_9_nao_repetido(self):
        num = randrange(9) + 1
        if num not in self.numeros_ja_gerados:
            self.numeros_ja_gerados.append(num)
            return num
        else:
            return self.numero_entre_1_e_9_nao_repetido()

    # Retorna uma matriz com 8 números entre 1 e 8, e um espaço vazio (None)
    # Ex:   [   [5, 3, 4],
    #           [2, None, 7],
    #           [1, 6, 8] 
    #       ]
    def gera_matriz_aleatoria(self):
        m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(m)):
            for j in range(len(m[i])):
                m[i][j] = self.numero_entre_1_e_9_nao_repetido()

        # Troca o 9 por None, que representará o estado vazio
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == 9:
                    m[i][j] = None

        return m