import random

class GeradorDeMatriz:

    # Retorna uma matriz com 8 números entre 1 e 8, e um espaço vazio (None)
    # Ex:   [   [5, 3, 4],
    #           [2, None, 7],
    #           [1, 6, 8]
    #       ]
    @staticmethod
    def gera_matriz_aleatoria():
        numeros_disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, None]
        random.shuffle(numeros_disponiveis)
        matriz = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = numeros_disponiveis.pop()
        return matriz

        
    # Matrizes rapidas feitas a mão
    # (chegarão ao fim com poucos movimentos)
    @staticmethod
    def matriz_rapida_1():
        return [
            [4, 1, 3],
            [7, None, 5],
            [8, 2, 6]
        ]
        
    @staticmethod
    def matriz_rapida_2():
        return [
            [None, 1, 3],
            [4, 7, 5],
            [8, 2, 6]
        ]
        
    @staticmethod
    def matriz_rapida_3():
        return [
            [1, 3, None],
            [4, 7, 5],
            [8, 2, 6]
        ]

    

    @staticmethod
    def matriz_final():
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, None]
        ]

