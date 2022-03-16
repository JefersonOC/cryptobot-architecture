import ccxt
from exchanges import exchange

from models.price import Price


class Binance(exchange.Exchange):
    def __init__(self, key: str, secret: str):
        super().__init__(key, secret)

        self.client = ccxt.binance({
            'apiKey': self.apiKey,
            'secret': self.apiSecret,
            'enableRateLimit': True,
        })

        self.name = self.__class__.__name__

    def get_client(self):
        return self.client

    def get_symbol(self):
        return self.currency + "/" + self.asset

    def symbol_ticker(self):
        try:
            response = self.client.fetch_ticker(self.get_symbol())
            return Price(pair=self.get_symbol(),
                         currency=self.currency.lower(),
                         asset=self.asset.lower(),
                         exchange=self.name.lower(),
                         current=response['last'])
        except Exception as error:
            print(str(error))

    def get_balance(self, currency):
        response = self.client.fetch_balance()["info"]["balances"]
        balances = [x for x in response if float(x['free']) > 0.0]
        balances_filtered = list(
            filter(lambda x: (x['asset'] == currency), balances))
        for balance in balances_filtered:
            return float(balance['free'])
