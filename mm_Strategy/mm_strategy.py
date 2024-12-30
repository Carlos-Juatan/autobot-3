
class MMStrategy:
    def __init__(self, data):
        self.data = data

    # Passo 3 - Calcular indicadores pro modelo
    def get_returned_metrics(self):
        self.data["retorno"] = self.data["Adj Close"].pct_change()
        return self.data["retorno"]

    def get_metrics(self):
        self.data["media_maxima"] = self.data["High"].rolling(window = 20).mean()
        self.data["media_minima"] = self.data["Low"].rolling(window = 20).mean()
        return self.data
    
    # Passo 4 - Gerar sinais de compra
    def generate_buy_signals(self):
        self.data["sinal_compra"] = 0
        self.data["sinal_compra"] = (self.data["Close"] > self.data["media_maxima"]).astype(int)
        return self.data

    # Passo 5 - Gerar sinais de venda
    def generate_sell_signals(self):
        self.data["sinal_venda"] = 0
        self.data["sinal_venda"] = (self.data["Close"] < self.data["media_minima"]).astype(int)
        return self.data