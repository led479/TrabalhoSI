class CalculadorHeuristica:

    def __init__(self, matriz):
        self.matriz = matriz

    def calcula_heuristica_simples(self):
        soma = 9
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                peca_atual = self.matriz[i][j]
                linha_final, coluna_final = self.posicoes_finais()[peca_atual]

                # Se a peça_atual está em sua posição final, retira 1
                if (i == linha_final and j == coluna_final):
                    soma -= 1
        return soma


    def calcula_heuristica_complexa(self):
        soma = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                peca_atual = self.matriz[i][j]
                linha_final, coluna_final = self.posicoes_finais()[peca_atual]

                # Distância da posição atual até a posição final da peça
                soma += abs(linha_final - i) + abs(coluna_final - j)
        return soma

    @staticmethod
    def posicoes_finais():
        return {
            1:    (0, 0),
            2:    (0, 1),
            3:    (0, 2),
            4:    (1, 0),
            5:    (1, 1),
            6:    (1, 2),
            7:    (2, 0),
            8:    (2, 1),
            None: (2, 2)
        }
