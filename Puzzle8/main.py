from classes.estado import Estado
from classes.controlador_Listas import Controlador_Listas
from classes.controlador_Buscas import Controlador_Buscas

print("==================== Métodos de busca ====================\n")
estado_inicial = Estado()
buscas = Controlador_Buscas(estado_inicial);
buscas.busca_custo_uniforme()

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