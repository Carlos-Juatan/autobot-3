import matplotlib.pyplot as plt
import mplcyberpunk
plt.style.use("cyberpunk")

from binanceAPI import BinanceAPI
from mm_strategy import MMStrategy





# Passo 6 - Gerar operações
def generate_position(data):
    data["posicao"] = 0

    for i in range(1, len(data)):
        if data["sinal_compra"].iloc[i] == 1:
            data["posicao"].iloc[i] = 1

        elif data["sinal_venda"].iloc[i] == 1:
            data["posicao"].iloc[i] = 0

        else:
            if (data["posicao"].iloc[i - 1] == 1) and (data["sinal_venda"].iloc[i] == 0):
                data["posicao"].iloc[i] = 1

            else:
                data["posicao"].iloc[i] = 0

    data["posicao"] = data["posicao"].shift()
    return data

# Passo 7 - Criar um ID para todos os trades históricos na tabela
def generate_id(data):
    data["trades"] = (data["posicao"] != data["posicao"].shift()).cumsum()
    data["trades"] = data["trades"].where(data["posicao"] == 1)
    data = data.dropna(subset = "trades")
    return data

# Passo 8 - Calcular retornos de todos os trades
def calculate_cumulative_return(data):
    value = (1 + data["retorno"]).cumprod() - 1
    return value

def get_equity_curve(returned_metrics):
    value = (1 + returned_metrics).cumprod() - 1
    return value

# Passo 9 - Gráfico de retornos
def show_graphics(cumulative_return, equity_curve):
    cumulative_return.plot(label = "Modelo")
    equity_curve.plot(label = tickerSymbo)
    plt.legend()

    plt.show()

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


# Passo 6 - Gerar operações
dados = generate_position(dados)

# Passo 7 - Criar um ID para todos os trades históricos na tabela
dados = generate_id(dados)

# Passo 8 - Calcular retornos de todos os trades
df_retorno_acumulado = calculate_cumulative_return(dados)
dados_retornos_completos_acum = get_equity_curve(dados_retornos_completos)


############### visualizer ###########################


# Passo 9 - Gráfico de retornos
show_graphics(df_retorno_acumulado, dados_retornos_completos_acum)