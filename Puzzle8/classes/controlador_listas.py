from operator import attrgetter
from classes.lista_ordenada import ListaOrdenada
from classes.estado import Estado

class ControladorListas:

    def __init__(self):
            self.estados_abertos = ListaOrdenada()
            self.estados_visitados = []

    def adiciona_estado_se_nao_for_conhecido(self, estado):
        if(self.__estado_ja_conhecido(estado) == False):
            self.estados_abertos.append(estado)
            return True
        return False
        
    def abir_nodo(self):
        estado_aberto = self.estados_abertos.lista.pop(0)
        self.estados_visitados.append(estado_aberto)
        return estado_aberto

    # Verifica se estado já conhecido, se já foi aberto e não foi visitado ou já foi visitado
    def __estado_ja_conhecido(self, estado):
        for estado_aberto in self.estados_abertos.lista:
            if(estado_aberto.matriz == estado.matriz):
                return True
        
        for estado_visitado in self.estados_visitados:
            if(estado_visitado.matriz == estado.matriz):
                return True

        return False