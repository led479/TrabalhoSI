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

        # Se estiver nas pontas e movimento estrapola o limite da matriz retornar None
        posicao_cima = self.validar_filho(posicao_vazio[0] - 1, posicao_vazio[1])
        posicao_direita = self.validar_filho(posicao_vazio[0], posicao_vazio[1] + 1)
        posicao_baixo = self.validar_filho(posicao_vazio[0] + 1, posicao_vazio[1])
        posicao_esquerda = self.validar_filho(posicao_vazio[0], posicao_vazio[1] - 1)

        movimentos = [posicao_cima, posicao_direita, posicao_baixo, posicao_esquerda]

        filhos = []

        # Para cada possivel movimento é gerado um filho
        for nova_posicao in movimentos:
            if(nova_posicao != None):
                filhos.append(self.gerar_filho(posicao_vazio, nova_posicao))

        return filhos

    def indice_do_vazio(self):
        for i in range(len(self.matriz)):
              for j in range(len(self.matriz[i])):
                  if(self.matriz[i][j] == None):
                      return [i, j]

    @staticmethod
    def estado_final():
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]
    # Verifica se proxima movimento estrapola o limite da matriz
    def validar_filho(self, linha, coluna):
        if(linha == -1 or linha == 3 or coluna == -1 or coluna == 3):
            return None
        return [linha, coluna]

    # Gera um filho de um estado, a próxima jogada
    def gerar_filho(self, posicao_vazio, nova_posicao):
        # Copia a matriz atual
        filho = deepcopy(self.matriz)
        ## ===================> Inicia o movimento da peça
        # Guarda o elemento da posição á qual será movido o espaço em branco
        elemento = filho[nova_posicao[0]][nova_posicao[1]]
        
        # Antigo espaço em branco recebe o elemento
        filho[posicao_vazio[0]][posicao_vazio[1]] = elemento

        # Inseri espaço em branco na nova posição
        filho[nova_posicao[0]][nova_posicao[1]] = None
        ## ===================>Finaliza o movimento da peça
        return filho