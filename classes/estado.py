from .gerador_de_matriz import GeradorDeMatriz
from copy import copy, deepcopy


class Estado:
    def __init__(self):
        self.matriz = GeradorDeMatriz().gera_matriz_aleatoria()

        # TODO Adicionar algoritmo para custo
        self.custo = None

        # TODO Adicionar algoritmo para heurística
        self.heuristica = None

    # TODO Já existem as posições por volta do espaço vazio, só falta fazer o método
    def filhos(self):
        posicao_vazio = self.indice_do_vazio()

        posicao_cima = [posicao_vazio[0] - 1, posicao_vazio[1]]
        posicao_direita = [posicao_vazio[0], posicao_vazio[1] + 1]
        posicao_baixo = [posicao_vazio[0] + 1, posicao_vazio[1]]
        posicao_esquerda = [posicao_vazio[0], posicao_vazio[1] - 1]

        return [posicao_cima,
                posicao_direita,
                posicao_baixo,
                posicao_esquerda]
        #if(posicao_vazio == [0, 0]):
         #   filho1 = deepcopy(self.matriz)
          #  filho1[0][0] = filho1[0][0 + 1]
           # filho1[0][0 + 1] = None
#
 #           filho2 = deepcopy(self.matriz)
  #          filho2[0][0] = filho2[0 + 1][0]
   #        filho2[0 + 1][0] = None
    #        return [filho1, filho2]
    #    else:
     #     return 'eae'



    def indice_do_vazio(self):
        for i in range(len(self.matriz)):
              for j in range(len(self.matriz[i])):
                  if(self.matriz[i][j] == None):
                      return [i, j]
        return []

    @staticmethod
    def estado_final():
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]