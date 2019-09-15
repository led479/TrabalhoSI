from classes.estado import Estado
from classes.controlador_Listas import Controlador_Listas
from copy import copy, deepcopy

class Controlador_Buscas:

    def __init__(self, estado_inicial):
        self.__estado_inicial = estado_inicial

    def busca_custo_uniforme(self):
        print("1º Método: Custo Uniforme (sem heurística)\n")
        print("===========================================================\n")

        print("Estado inicial:")
        self.imprimir_Estado(self.__estado_inicial)
        lista_nodos = Controlador_Listas()

        lista_nodos.adicionar_estado_abertos(self.__estado_inicial, 0)
        
        while(True):
            nodo_aberto = lista_nodos.abir_nodo()
            # Fazer a verificação
            if(nodo_aberto.matriz != self.__estado_final()):
                print("\nNão é o estado final. Gerando filhos...")
                filhos = self.__filhos(nodo_aberto)
                for filho in filhos:
                    lista_nodos.adicionar_estado_abertos(filho, 1)
                    print("\n========================== FILHO ==========================")
                    self.imprimir_Estado(filho)
            else:
                # Exibir os resultados
                print("Encontrou estado final....")

        #nodo_aberto = lista_nodos.abir_nodo()

        ## Fazer a verificação
        #if(nodo_aberto.matriz != self.__estado_final()):
        #    print("\nNão é o estado final. Gerando filhos...")
        #    filhos = self.__filhos(nodo_aberto)
        #    for filho in filhos:
        #        lista_nodos.adicionar_estado_abertos(filho, 1)
        #        print("\n========================== FILHO ==========================")
        #        self.imprimir_Estado(filho)
        #else:
        #    # Exibir os resultados
        #    print("Encontrou estado final....")


     # Gera Matriz para Imprimir 
    def imprimir_Estado(self, estado):
        print(f"                {estado.matriz[0]}")
        print(f"                {estado.matriz[1]}")
        print(f"                {estado.matriz[2]}")

    # Estado final do objeto
    def __estado_final(self):
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]


    def __filhos(self, nodo):
        posicao_vazio = nodo.indice_do_vazio()

        # Se estiver nas pontas e o movimento estrapolar o limite da matriz retornar None
        posicao_cima = self.__validar_movimento(posicao_vazio[0] - 1, posicao_vazio[1])
        posicao_direita = self.__validar_movimento(posicao_vazio[0], posicao_vazio[1] + 1)
        posicao_baixo = self.__validar_movimento(posicao_vazio[0] + 1, posicao_vazio[1])
        posicao_esquerda = self.__validar_movimento(posicao_vazio[0], posicao_vazio[1] - 1)

        movimentos = [posicao_cima, posicao_direita, posicao_baixo, posicao_esquerda]

        filhos = []

        # Para cada possivel movimento é gerado um filho
        for movimento in movimentos:
            if(movimento != None):
                filhos.append(self.__gerar_filho(posicao_vazio, movimento, nodo))
        return filhos

    # Verifica se proxima movimento estrapola o limite da matriz
    def __validar_movimento(self, linha, coluna):
        if(linha == -1 or linha == 3 or coluna == -1 or coluna == 3):
            return None
        return [linha, coluna]


    # Gera um filho de um estado, a próxima jogada
    def __gerar_filho(self, posicao_vazio, movimento, nodo):
        # Copia a matriz atual
        filho = deepcopy(nodo)
        ## ===================> Inicia o movimento da peça
        # Guarda o elemento da posição á qual será movido o espaço em branco
        elemento = filho.matriz[movimento[0]][movimento[1]]
        
        # Antigo espaço em branco recebe o elemento
        filho.matriz[posicao_vazio[0]][posicao_vazio[1]] = elemento

        # Inseri espaço em branco na nova posição
        filho.matriz[movimento[0]][movimento[1]] = None
        ## ===================>Finaliza o movimento da peça
        return filho