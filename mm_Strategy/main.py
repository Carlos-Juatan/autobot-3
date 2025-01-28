

from binanceAPI import BinanceAPI
from mm_strategy import MMStrategy
from backtester import Backtester
from visualizer import Visualizer


############### pegando dados ###########################


# Passo 2 - Pegar dados de cotação do Yahoo Finance
tickerSymbo = "BTC-USD"
client = BinanceAPI()
dados = client.fetch_yahoo_data(tickerSymbo, "2000-01-01", "2024-11-30")
print(dados)

# Passo 3 - Calcular indicadores pro modelo
strategy = MMStrategy(dados)
dados_retornos_completos = strategy.get_returned_metrics()
dados = strategy.get_metrics()

# Passo 4 - Gerar sinais de compra
dados = strategy.generate_buy_signals()

# Passo 5 - Gerar sinais de venda
dados = strategy.generate_sell_signals()


############### Backtest ###########################


backtest = Backtester(dados)

# Passo 6 - Gerar operações
dados = backtest.generate_position()

# Passo 7 - Criar um ID para todos os trades históricos na tabela
dados = backtest.generate_id()

# Passo 8 - Calcular retornos de todos os trades
df_retorno_acumulado = (1 + dados["retorno"]).cumprod() - 1
dados_retornos_completos_acum = (1 + dados_retornos_completos).cumprod() - 1


############### visualizer ###########################


visualizer = Visualizer()

# Passo 9 - Gráfico de retornos
visualizer.show_graphics(df_retorno_acumulado, dados_retornos_completos_acum, tickerSymbo)