import yfinance as yf

class BinanceAPI:
    # Passo 2 - Pegar dados de cotação do Yahoo Finance
    def fetch_yahoo_data(self, ticker, startTime, endTime):
        self.data = yf.download(ticker, startTime, endTime)
        self.data = self.data.droplevel(1, axis = 1)
        return self.data