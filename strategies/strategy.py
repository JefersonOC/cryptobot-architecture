from abc import ABC, abstractmethod
from models.price import Price
import time
import threading


class Strategy(ABC):
    price: Price

    def __init__(self, exchange, interval=60):
        self.exchange = exchange
        self.is_running = False
        self._timer = None
        self.interval = interval
        self.next_call = time.time()

    def get_price(self):
        return self.price

    def set_price(self, price: Price):
        self.price = price

    def start(self):
        if not self.is_running:
            if self._timer is None:
                # primeira vez já executa
                self.next_call = time.time()
            else:
                # adiciona intervalo para a próxima execução
                self.next_call += self.interval

            # cria thread para execução do metodo _run
            self._timer = threading.Timer(
                self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.start()
        self.set_price(self.exchange.symbol_ticker())
        self.run()

    # abstract methods
    @abstractmethod
    def run(self):
        pass
