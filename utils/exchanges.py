import logging
from binance.client import Client as BinanceClient
from coinex.client import Client as CoinExClient
from bybit import Client as BybitClient
from bitget.client import Client as BitgetClient

class ExchangeHandler:
    def __init__(self, config):
        self.exchanges = {
            'binance': BinanceClient(api_key=config['binance']['api_key'], api_secret=config['binance']['api_secret']),
            'coinex': CoinExClient(api_key=config['coinex']['api_key'], api_secret=config['coinex']['api_secret']),
            'bybit': BybitClient(api_key=config['bybit']['api_key'], api_secret=config['bybit']['api_secret']),
            'bitget': BitgetClient(api_key=config['bitget']['api_key'], api_secret=config['bitget']['api_secret']),
        }

    def buy_usdt(self, exchange_name, amount_inr):
        exchange = self.exchanges.get(exchange_name)
        if not exchange:
            logging.error(f"Exchange {exchange_name} not supported.")
            return None

        usdt_amount = amount_inr / 82  # Example conversion rate
        logging.info(f"Buying {usdt_amount} USDT on {exchange_name}.")

        try:
            order = exchange.order_market_buy(
                symbol='USDTINR',
                quantity=usdt_amount
            )
            logging.info(f"USDT purchase successful on {exchange_name}. Order: {order}")
            return order
        except Exception as e:
            logging.error(f"Failed to purchase USDT on {exchange_name}. Error: {e}")
            return None
