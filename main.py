import sys
from decouple import config
import importlib
import signal
import threading
import pandas as pd

# ENV
exchange_name = config('EXCHANGE')
strategy: str = config('STRATEGY')
interval: int = int(config('INTERVAL'))
key: str = config(exchange_name.upper() + '_API_KEY')
secret: str = config(exchange_name.upper() + '_API_SECRET')

# PAIR
currency: str = config('CURRENCY')
asset: str = config('ASSET')


print("#######################################")
print("######  CRYPTOBOT ARCHITECTURE  #######")
print("#########    BLACKFISH LABS   #########")
print("#######################################")

# CARREGAR EXCHANGE
print("Connecting to {} exchange...".format(exchange_name.upper()))
exchangeModule = importlib.import_module(
    'exchanges.' + exchange_name, package=None)
exchangeClass = getattr(
    exchangeModule, exchange_name[0].upper() + exchange_name[1:])
exchange = exchangeClass(key, secret)

# CARREGAR OS PARES DE MOEDAS PARA NEGOCIAÇÃO
exchange.set_currency(currency)
exchange.set_asset(asset)

# CARREGAR A ESTRATÉGIA DE TRADING
strategyModule = importlib.import_module(
    'strategies.' + strategy, package=None)
strategyClass = getattr(
    strategyModule, strategy[0].upper() + strategy[1:])

# CARREGAR CONFIGURAÇÕES SE NECESSÁRIO
if strategy == "logger":
    my_strategy = strategyClass(exchange, interval)
    print("Logger Strategy Working")

# CARREGAR ESTRATÉGIA NA EXCHANGE
exchange.set_strategy(my_strategy)

# EXECUÇÃO
print("{} mode on {} pair".format("Live", exchange.get_symbol()))
print("--------------------------------------")
exchange.strategy.start()


def signal_handler(signal, frame):
    print('stopping strategy...')
    exchange.strategy.stop()
    sys.exit(0)


# SIGINT É O SINAL DE INTERRUPÇÃO (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)
forever = threading.Event()
forever.wait()
exchange.strategy.stop()
sys.exit(0)
