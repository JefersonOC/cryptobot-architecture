# cryptobot-architecture
A architecture to build a crypto bot with Python 3 and the Binance API
## Desenvolvedor
Jeferson Cruz
## Tecnologia
Python
```
sudo apt-get install python3-lxml
pip install -r requirements.txt
```
**LOGGER**
```
STRATEGY=logger INTERVAL=5 CURRENCY=BTC ASSET=BUSD python3 -B main.py
STRATEGY=logger INTERVAL=5 CURRENCY=BTC ASSET=BUSD pm2 start main.py --name BOT-WATCH-BTC --interpreter python3
```