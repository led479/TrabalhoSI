from classes.calculador_heuristica import CalculadorHeuristica
from enums.tipo_heuristica import TipoHeuristica
from copy import deepcopy

class Estado:
    def __init__(self, matriz, tipo_heuristica, pai=None):
        self.matriz = matriz
        self.pai = pai
        self.custo = pai.custo + 1 if pai else 0

        self.tipo_heuristica = tipo_heuristica

        if   tipo_heuristica == TipoHeuristica.sem:
            self.heuristica = 0
        elif tipo_heuristica == TipoHeuristica.simples:
            self.heuristica = CalculadorHeuristica(self.matriz).calcula_heuristica_simples()
        elif tipo_heuristica == TipoHeuristica.complexa:
            self.heuristica = CalculadorHeuristica(self.matriz).calcula_heuristica_complexa()

        self.custo_total = self.custo + self.heuristica

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
        # Cria uma nova matriz trocando as posições do None com a peça na posição do movimento
        matriz = deepcopy(self.matriz)
        matriz[posicao_vazio['linha']][posicao_vazio['coluna']] = matriz[movimento['linha']][movimento['coluna']]
        matriz[movimento['linha']][movimento['coluna']] = None

        filho = Estado(matriz, self.tipo_heuristica, self)

        return filho