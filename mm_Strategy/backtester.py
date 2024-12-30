class Backtester:
    def __init__(self, data):
        self.data = data  # Avoid modifying original self.self.data
        # self.indicators = indicators.copy()
        # self.initial_value = initial_value
        # self.quantity = quantity
        # self.fee = fee


    # Passo 6 - Gerar operações
    def generate_position(self):
        self.data["posicao"] = 0

        for i in range(1, len(self.data)):
            if self.data["sinal_compra"].iloc[i] == 1:
                self.data["posicao"].iloc[i] = 1

            elif self.data["sinal_venda"].iloc[i] == 1:
                self.data["posicao"].iloc[i] = 0

            else:
                if (self.data["posicao"].iloc[i - 1] == 1) and (self.data["sinal_venda"].iloc[i] == 0):
                    self.data["posicao"].iloc[i] = 1

                else:
                    self.data["posicao"].iloc[i] = 0

        self.data["posicao"] = self.data["posicao"].shift()
        return self.data

    # Passo 7 - Criar um ID para todos os trades históricos na tabela
    def generate_id(self):
        self.data["trades"] = (self.data["posicao"] != self.data["posicao"].shift()).cumsum()
        self.data["trades"] = self.data["trades"].where(self.data["posicao"] == 1)
        value = self.data.dropna(subset = "trades")
        return value