from classes.estado import Estado
from classes.controlador_listas import ControladorListas
from copy import deepcopy

class ControladorBuscas:

    def __init__(self, estado_inicial):
        self.__estado_inicial = estado_inicial

    def busca_custo_uniforme(self):

        print("1º Método: Custo Uniforme (sem heurística)\n")
        print("===========================================================\n")
        print("Estado inicial:")
        self.imprime_matriz(self.__estado_inicial)

        listas = ControladorListas()
        listas.adiciona_estado_se_nao_for_conhecido(self.__estado_inicial)

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
        print("Encontrou estado final!!")



     # Gera Matriz para Imprimir 
    def imprime_matriz(self, estado):
        print(estado.matriz[0])
        print(estado.matriz[1])
        print(estado.matriz[2])

    # Estado final do objeto
    def __matriz_final(self):
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]