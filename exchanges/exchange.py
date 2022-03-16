from abc import ABC, abstractmethod
from strategies.strategy import Strategy


class Exchange(ABC):
    currency: str
    asset: str
    strategy: Strategy

    def __init__(self, key: str, secret: str):
        self.apiKey = key
        self.apiSecret = secret
        self.name = None
        self.currency = ''
        self.asset = ''
        self.strategy = None

    def set_currency(self, symbol: str):
        self.currency = symbol

    def set_asset(self, symbol: str):
        self.asset = symbol

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy

    def format_pair(self):
        return self.currency + "/" + self.asset

    # abstract methods
    @abstractmethod
    def get_symbol(self):
        return self.format_pair(self)
