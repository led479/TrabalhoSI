class CalculadorHeuristica:

    def __init__(self, matriz):
        self.matriz = matriz

    def calcula_heuristica_simples(self):
        soma = 9
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                peca_atual = self.matriz[i][j]
                posicao_final = self.posicoes_finais()[peca_atual]

                # Se a peça_atual está em sua posição final, retira 1
                if (i == posicao_final['linha'] and j == posicao_final['coluna']):
                    soma -= 1
        return soma


    def calcula_heuristica_complexa(self):
        soma = 0
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                peca_atual = self.matriz[i][j]
                posicao_final = self.posicoes_finais()[peca_atual]

                # Distância da posição atual até a posição final da peça
                soma += abs(posicao_final['linha'] - i) + abs(posicao_final['coluna'] - j)
        return soma

    @staticmethod
    def posicoes_finais():
        return {
            1:    { 'linha': 0, 'coluna': 0 },
            2:    { 'linha': 0, 'coluna': 1 },
            3:    { 'linha': 0, 'coluna': 2 },
            4:    { 'linha': 1, 'coluna': 0 },
            5:    { 'linha': 1, 'coluna': 1 },
            6:    { 'linha': 1, 'coluna': 2 },
            7:    { 'linha': 2, 'coluna': 0 },
            8:    { 'linha': 2, 'coluna': 1 },
            None: { 'linha': 2, 'coluna': 2 },
        }
