from classes.estado import Estado
from classes.controlador_buscas import ControladorBuscas
from enums.tipo_matriz import TipoMatriz

############################################################################################
# Escolha do tipo de matriz
# Algoritmo muito lento para matriz aleatória;
# Foram feitas algumas matrizes na mão para rodar em tempo hábil...
# matriz_inical = GeradorDeMatriz.gera_matriz_aleatoria()
while(True):
    print("============================= Tipo de Matriz =============================\n")
    print("1 | Matriz: Aleatoria: O Algorítmo pode gerar uma matriz sem solução.")
    print("2 | Matriz: Rapida 1: Matriz que possui um estado final.")
    print("3 | Matriz: Rapida 2: Matriz que possui um estado final.")
    print("4 | Matriz: Rapida 3: Matriz que possui um estado final.")
    print("0 | Sair.")
    print("\n=======================================================================\n")

    tipo_matriz = eval(input("Qual tipo de matriz deseja executar [1|2|3|4]: "))
    while (tipo_matriz < 0 or tipo_matriz > 4):
        print("Opção inválida!")
        tipo_buca = eval(input("Qual tipo de matriz deseja executar [1|2|3|4]: "))
    else:
        if(tipo_matriz == 1):
            buscas = ControladorBuscas(TipoMatriz.aleatoria)
        elif(tipo_matriz == 2):
            buscas = ControladorBuscas(TipoMatriz.rapida1)
        elif(tipo_matriz == 3):
            buscas = ControladorBuscas(TipoMatriz.rapida2)
        elif(tipo_matriz == 4):
            buscas = ControladorBuscas(TipoMatriz.rapida3)
        elif(tipo_matriz == 0):
            exit("By")
            break

    ############################################################################################
    # Escolha do tipo de algoritmo
    print("\n=========================== Métodos de busca ===========================\n")
    print("1 | Método: Busca Com Custo Uniforme.")
    print("2 | Método: Busca Com Heurística Simples.")
    print("3 | Método: Busca Com Heurística Complexa.")
    print("0 | Sair.")
    print("\n========================================================================\n")

    tipo_buca = eval(input("Qual método de busca deseja executar [1|2|3]: "))
    while(tipo_buca < 0 or tipo_buca > 3):
        print("Opção inválida!")
        tipo_buca = eval(input("Qual método de busca deseja executar [1|2|3]: "))
    else:
        if(tipo_buca == 1):
            buscas.busca_custo_uniforme()
        elif(tipo_buca == 2):
            buscas.busca_com_heuristica_simples()
        elif(tipo_buca == 3):
            buscas.busca_com_heuristica_complexa()
        elif(tipo_buca == 4):
            exit("By2")
            break
    print("\n============================================================================================================")
    nova_busca = input("\nDeseja executar novamente ? Digite 'SIM' ou aperte qualquer tecla para encerrar o programa: ")
    if(nova_busca != "SIM" and nova_busca != "sim" and nova_busca != "S" and nova_busca != "s"):
        break


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