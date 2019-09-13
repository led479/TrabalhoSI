from .gerador_de_matriz import GeradorDeMatriz

class Estado:
    def __init__(self):
        self.matriz = GeradorDeMatriz().gera_matriz_aleatoria()

        # TODO Adicionar algoritmo para custo
        self.custo = None

        # TODO Adicionar algoritmo para heurística
        self.heuristica = None

    @staticmethod
    def estado_final():
        return [  [1, 2, 3],
                  [4, 5, 6],
                  [7, 8, None]
                ]