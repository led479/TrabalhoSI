from classes.estado import Estado
from classes.controlador_buscas import ControladorBuscas

print("==================== Métodos de busca ====================\n")
# Algoritmo muito lento para matriz aleatória;
# Foram feitas algumas matrizes na mão para rodar em tempo hábil...
# matriz_inical = GeradorDeMatriz.gera_matriz_aleatoria()


buscas = ControladorBuscas()
#buscas.busca_custo_uniforme()
buscas.busca_com_heuristica()


#A entrada do programa é um tabuleiro desordenado (com o quadrado sem número em qualquer lugar do tabuleiro).
#A saída principal do programa é o menor caminho (a sequência de movimentos do quadrado sem número)
# para chegar-se ao tabuleiro ordenado. Além do caminho, deve ser exibido:

#a)O total de nodos visitados
#b)O maior tamanho da fronteira durante a busca
#c)O tamanho do caminho

#for filhos in e.filhos():
#    print("-------FILHO-------")
#    print(filhos[0])
#    print(filhos[1])
#    print(filhos[2])