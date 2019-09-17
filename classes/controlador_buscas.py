from classes.estado import Estado
from classes.controlador_listas import ControladorListas
from classes.gerador_de_matriz import GeradorDeMatriz
from enums.tipo_heuristica import TipoHeuristica

from copy import deepcopy
import time


class ControladorBuscas:

    def __init__(self):
        self.matriz_inical = GeradorDeMatriz.matriz_rapida_3()

    def busca_custo_uniforme(self):
        print("1º Método: Custo Uniforme (sem heurística)\n")
        print("===========================================================\n")
        estado_inicial = Estado(self.matriz_inical, TipoHeuristica.sem)
        self.busca(estado_inicial)

    def busca_com_heuristica_simples(self):
        print("2º Método: Busca com Heurística Simples\n")
        print("===========================================================\n")
        estado_inicial = Estado(self.matriz_inical, TipoHeuristica.simples)
        self.busca(estado_inicial)

    def busca_com_heuristica_complexa(self):
        print("3º Método: Busca com Heurística Complexa\n")
        print("===========================================================\n")
        estado_inicial = Estado(self.matriz_inical, TipoHeuristica.complexa)
        self.busca(estado_inicial)


    def busca(self, estado_inicial):

        print('Buscando...')
        start = time.time()

        listas = ControladorListas()
        listas.adiciona_estado_se_nao_for_conhecido(estado_inicial)

        estado_aberto = listas.abir_nodo()
        while(estado_aberto.matriz != self.__matriz_final()):
            filhos = estado_aberto.filhos()
            for filho in filhos:
                listas.adiciona_estado_se_nao_for_conhecido(filho)

            estado_aberto = listas.abir_nodo()

        # Exibir os resultados
        print('Terminou!')
        end = time.time()
        self.imprime_caminho(estado_aberto)
        print(f"\nCUSTO ESTADO FINAL: {estado_aberto.custo}")
        print(f"NODOS ABERTOS: {len(listas.estados_abertos.lista)}")
        print(f"NODOS VISITADOS: {len(listas.estados_visitados)}")
        print(f"Algoritmo levou {end - start} segundos")

    # Gera Matriz para Imprimir
    def imprime_matriz(self, estado):
        print(estado.matriz[0])
        print(estado.matriz[1])
        print(estado.matriz[2])
        print("--------------")

    def imprime_caminho(self, estado):
        atual = estado
        print('=========CAMINHO==========')
        while(atual):
            print(f"Custo: {atual.custo}")
            print(f"Valor Heurística: {atual.heuristica}")
            print(f"Custo total (custo + heurística): {atual.custo + atual.heuristica}")
            self.imprime_matriz(atual)
            atual = atual.pai
        print('==========FIM-CAMINHO============')

    # Estado final do objeto
    def __matriz_final(self):
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]