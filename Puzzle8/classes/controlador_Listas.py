
class Controlador_Listas:

    def __init__(self):
            self.__nodos_abertos = []
            self.__nodos_visitados = []

    def adicionar_estado_abertos(self, estado, custo):
        
        self.__nodos_abertos.append(estado)
        estado.custo+=custo
        

    def abir_nodo(self):
        nodo_aberto = self.__nodos_abertos.pop(0)
        self.__nodos_visitados.append(nodo_aberto)
        return nodo_aberto

    def __nodo_ja_aberto():
        pass

    
