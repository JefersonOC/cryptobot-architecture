from exchanges.exchange import Exchange
from strategies.strategy import Strategy
from datetime import datetime


class Logger(Strategy):
    def __init__(self, exchange: Exchange, timeout=60):
        super().__init__(exchange, timeout)

    def run(self):
        print(datetime.now())
        print('--------------------------------------')
        print('Exchange: ' + self.exchange.name)
        print('Pair: ' + self.exchange.get_symbol())
        print('Price: ' + str(round(self.price.current, 2)))
        try:
            print('Available Currency: ' + str(self.exchange.get_balance(
                self.exchange.currency)) + ' ' + self.exchange.currency)
            print('Available Asset: ' + str(round(self.exchange.get_balance(
                self.exchange.asset))) + ' ' + self.exchange.asset)
            print('--------------------------------------')
        except (TypeError):
            print('Positionless')
