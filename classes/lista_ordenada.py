class ListaOrdenada(list):

    def append(self, estado):
        super().append(estado)
        self.sort(key=lambda x: x.custo_total)