from operator import attrgetter
from classes.estado import Estado

class Controlador_Listas:

    def __init__(self):
            self.__estados_abertos = []
            self.__estados_visitados = []

    def adicionar_estado_abertos(self, estado):
        if(self.__estado_ja_conhecido(estado) == False):
            self.__estados_abertos.append(estado)
            self.__estados_abertos.sort(key=attrgetter("custo"))
            return True
        return False
        
    def abir_nodo(self):
        estado_aberto = self.__estados_abertos.pop(0)
        self.__estados_visitados.append(estado_aberto)
        return estado_aberto

    # Verifica se estado já conhecido, se já foi aberto e não foi visitado ou já foi visitado
    def __estado_ja_conhecido(self, estado):

        ## Verifica se estado já foi aberto mas não visitado
        for estado_em_aberto in self.__estados_abertos:
            if(self.__comparar_estados(estado_em_aberto, estado)):
                return True
        
        # Verifica se estado já foi visitado
        for estado_visitado in self.__estados_visitados:
            if(self.__comparar_estados(estado_visitado, estado)):
                return True

        return False

    def __comparar_estados(self, estado1, estado2):
        for i in range(len(estado1.matriz)):
                for j in range(len(estado1.matriz[i])):
                    if (estado1.matriz[i][j] != estado2.matriz[i][j]):
                        return False
        return True
