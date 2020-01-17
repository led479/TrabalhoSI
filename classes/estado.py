from classes.calculador_heuristica import CalculadorHeuristica
from enums.tipo_heuristica import TipoHeuristica
from copy import deepcopy

class Estado:
    def __init__(self, matriz, tipo_heuristica, pai=None):
        self.matriz = matriz
        self.pai = pai
        self.custo = pai.custo + 1 if pai else 0

        self.tipo_heuristica = tipo_heuristica

        self.heuristica = {
            TipoHeuristica.sem: self.__return_0,
            TipoHeuristica.simples: CalculadorHeuristica(self.matriz).calcula_heuristica_simples,
            TipoHeuristica.complexa: CalculadorHeuristica(self.matriz).calcula_heuristica_complexa
        }[tipo_heuristica]()

        self.custo_total = self.custo + self.heuristica

    def filhos(self):
        posicao_vazio = self.__indice_do_vazio()
        linha_vazio, coluna_vazio = posicao_vazio

        # Se estiver nas pontas e o movimento estrapolar o limite da matriz retornar None
        posicao_cima = self.__validar_movimento(linha_vazio - 1, coluna_vazio)
        posicao_direita = self.__validar_movimento(linha_vazio, coluna_vazio + 1)
        posicao_baixo = self.__validar_movimento(linha_vazio + 1, coluna_vazio)
        posicao_esquerda = self.__validar_movimento(linha_vazio, coluna_vazio - 1)

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
                    return i, j

    # Verifica se proxima movimento estrapola o limite da matriz
    def __validar_movimento(self, linha, coluna):
        if(linha == -1 or linha == 3 or coluna == -1 or coluna == 3):
            return None
        return linha, coluna


    # Gera um filho de um estado, a próxima jogada
    def __gera_filho(self, posicao_vazio, movimento):
        linha_vazio, coluna_vazio = posicao_vazio
        linha_movimento, coluna_movimento = movimento
        
        # Cria uma nova matriz trocando as posições do None com a peça na posição do movimento
        matriz = deepcopy(self.matriz)
        matriz[linha_vazio][coluna_vazio], matriz[linha_movimento][coluna_movimento] = matriz[linha_movimento][coluna_movimento], None

        filho = Estado(matriz, self.tipo_heuristica, self)

        return filho

    def __return_0(self):
        return 0