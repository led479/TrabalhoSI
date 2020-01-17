from classes.estado import Estado
from classes.controlador_listas import ControladorListas
from classes.gerador_de_matriz import GeradorDeMatriz
from enums.tipo_heuristica import TipoHeuristica
from enums.tipo_matriz import TipoMatriz
from copy import deepcopy
import time


class ControladorBuscas:

    def __init__(self, tipo_matriz):
        self.matriz_inicial = self.gerar_matriz(tipo_matriz)

    def gerar_matriz(self, tipo_matriz):
        return {
            TipoMatriz.aleatoria: GeradorDeMatriz().gera_matriz_aleatoria,
            TipoMatriz.rapida1: GeradorDeMatriz().matriz_rapida_1,
            TipoMatriz.rapida2: GeradorDeMatriz().matriz_rapida_2,
            TipoMatriz.rapida3: GeradorDeMatriz().matriz_rapida_3
        }[tipo_matriz]()

    def busca_custo_uniforme(self):
        print("\n========================================================================")
        print("================== Método: Custo Uniforme (sem heurística) =============")
        print("========================================================================\n")
        estado_inicial = Estado(self.matriz_inicial, TipoHeuristica.sem)
        self.busca(estado_inicial)

    def busca_com_heuristica_simples(self):
        print("\n========================================================================")
        print("================== Método: Busca com Heurística Simples ================")
        print("========================================================================\n")
        estado_inicial = Estado(self.matriz_inicial, TipoHeuristica.simples)
        self.busca(estado_inicial)

    def busca_com_heuristica_complexa(self):
        print("\n========================================================================")
        print("================ Método: Busca com Heurística Complexa =================")
        print("========================================================================\n")
        estado_inicial = Estado(self.matriz_inicial, TipoHeuristica.complexa)
        self.busca(estado_inicial)


    def busca(self, estado_inicial):

        print('Buscando...\n')
        start = time.time()

        listas = ControladorListas()
        listas.adiciona_estado_se_nao_for_conhecido(estado_inicial)

        estado_aberto = listas.abir_nodo()
        matriz_final = GeradorDeMatriz().matriz_final()
        while(estado_aberto.matriz != matriz_final):
            filhos = estado_aberto.filhos()
            for filho in filhos:
                listas.adiciona_estado_se_nao_for_conhecido(filho)

            estado_aberto = listas.abir_nodo()

        # Exibir os resultados
        print('Terminou!\n')
        end = time.time()
        self.imprime_caminho(estado_aberto)
        print(f"\nCUSTO (TAMANHO): {estado_aberto.custo}")
        print(f"NODOS ABERTOS: {len(listas.estados_abertos)}")
        print(f"NODOS VISITADOS: {len(listas.estados_visitados)}")
        print(f"Algoritmo levou {end - start} segundos")

    # Gera Matriz para Imprimir
    def imprime_matriz(self, estado):
        print(estado.matriz[0])
        print(estado.matriz[1])
        print(estado.matriz[2])
        print("-------------------------------------")

    def imprime_caminho(self, estado):
        atual = estado
        caminho_ordenado = []
        while(atual):
            caminho_ordenado.insert(0, atual)
            atual = atual.pai
        
        print('============== CAMINHO ==============\n')
        for atual in caminho_ordenado:
            print(f"Custo: {atual.custo}")
            print(f"Valor Heurística: {atual.heuristica}")
            print(f"Custo total (custo + heurística): {atual.custo + atual.heuristica}")
            self.imprime_matriz(atual)
        print('\n============ FIM CAMINHO ============')