from classes.estado import Estado
from classes.controlador_listas import ControladorListas
from classes.gerador_de_matriz import GeradorDeMatriz
from copy import deepcopy

class ControladorBuscas:

    def __init__(self):
        self.matriz_inical = GeradorDeMatriz.matriz_rapida_3()

    def busca_custo_uniforme(self):
        print("1º Método: Custo Uniforme (sem heurística)\n")
        print("===========================================================\n")
        print("Estado inicial:")
        estado_inicial = Estado(self.matriz_inical)
        self.busca(estado_inicial)

    def busca_com_heuristica(self):
        print("2º Método: Busca com Heurística\n")
        print("===========================================================\n")
        print("Estado inicial:")
        estado_inicial_com_heuristica = Estado(self.matriz_inical, None, True)        
        self.busca(estado_inicial_com_heuristica)

        

    def busca(self, estado_inicial):
        listas = ControladorListas()
        listas.adiciona_estado_se_nao_for_conhecido(estado_inicial)

        estado_aberto = listas.abir_nodo()
        while(estado_aberto.matriz != self.__matriz_final()):

            self.imprime_matriz(estado_aberto)

            filhos = estado_aberto.filhos()
            for filho in filhos:
                listas.adiciona_estado_se_nao_for_conhecido(filho)

            estado_aberto = listas.abir_nodo()

            print(f"\nCUSTO ESTADO: {estado_aberto.custo}")
            print(f"NODOS ABERTOS: {len(listas.estados_abertos.lista)}")
            print(f"NODOS VISITADOS: {len(listas.estados_visitados)}")

        # Exibir os resultados
        print('========================')
        print("Encontrou estado final!!")
        self.imprime_caminho(estado_aberto)
        print('========================')

    # Gera Matriz para Imprimir
    def imprime_matriz(self, estado):
        print(estado.matriz[0])
        print(estado.matriz[1])
        print(estado.matriz[2])
        print("--------------")

    def imprime_caminho(self, estado):
        atual = estado
        while(atual):
            print("Custo: " + str(atual.custo))
            print("Valor Heurística: " + str(atual.heuristica))
            self.imprime_matriz(atual)
            atual = atual.pai

    # Estado final do objeto
    def __matriz_final(self):
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]