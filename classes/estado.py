from classes.gerador_de_matriz import GeradorDeMatriz
from copy import deepcopy

class Estado:
    def __init__(self):
        # Algoritmo muito lento para matriz aleatória;
        # Foram feitas algumas matrizes na mão para rodar em tempo hábil...
        # self.matriz = GeradorDeMatriz.gera_matriz_aleatoria()

        # self.matriz = GeradorDeMatriz.matriz_final()
        # self.matriz = GeradorDeMatriz.matriz_rapida_1()
        # self.matriz = GeradorDeMatriz.matriz_rapida_2()
        self.matriz = GeradorDeMatriz.matriz_rapida_3()

        # Guarda Instância do estado Pai
        self.pai = None

        self.custo = 0

        # TODO Adicionar algoritmo para heurística
        self.heuristica = None


    def filhos(self):
        posicao_vazio = self.__indice_do_vazio()

        # Se estiver nas pontas e o movimento estrapolar o limite da matriz retornar None
        posicao_cima = self.__validar_movimento(posicao_vazio['linha'] - 1, posicao_vazio['coluna'])
        posicao_direita = self.__validar_movimento(posicao_vazio['linha'], posicao_vazio['coluna'] + 1)
        posicao_baixo = self.__validar_movimento(posicao_vazio['linha'] + 1, posicao_vazio['coluna'])
        posicao_esquerda = self.__validar_movimento(posicao_vazio['linha'], posicao_vazio['coluna'] - 1)

        movimentos = [posicao_cima, posicao_direita, posicao_baixo, posicao_esquerda]

        filhos = []

        # Para cada possivel movimento é gerado um filho
        for movimento in movimentos:
            if(movimento):
                filhos.append(self.__gera_filho(posicao_vazio, movimento))
        return filhos

    def __indice_do_vazio(self):
        for i in range(len(self.matriz)):
              for j in range(len(self.matriz[i])):
                  if(self.matriz[i][j] == None):
                      return { 'linha': i, 'coluna': j }


    # Verifica se proxima movimento estrapola o limite da matriz
    def __validar_movimento(self, linha, coluna):
        if(linha == -1 or linha == 3 or coluna == -1 or coluna == 3):
            return None
        return { 'linha': linha, 'coluna': coluna }


    # Gera um filho de um estado, a próxima jogada
    def __gera_filho(self, posicao_vazio, movimento):
        
        # Copia a matriz atual
        filho = deepcopy(self)
        ## ===================> Inicia o movimento da peça
        
        # Antigo espaço em branco recebe o elemento
        filho.matriz[posicao_vazio['linha']][posicao_vazio['coluna']] = filho.matriz[movimento['linha']][movimento['coluna']]

        # Insere espaço em branco na nova posição
        filho.matriz[movimento['linha']][movimento['coluna']] = None

        filho.pai = self
        filho.custo = self.custo + 1
        
        ## ===================>Finaliza o movimento da peça
        return filho
    