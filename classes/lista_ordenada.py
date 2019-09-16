from operator import attrgetter

class ListaOrdenada:

    def __init__(self):
        self.lista = []

    def append(self, estado):
        self.lista.append(estado)
        self.lista.sort(key=attrgetter("custo_total"))

