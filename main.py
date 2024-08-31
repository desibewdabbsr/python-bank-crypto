import yaml
import time
import logging
from utils.logging_config import setup_logging
from utils.exchanges import ExchangeHandler
from utils.payments import PaymentHandler
from telegram_bot import TelegramBot

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

def main():
    setup_logging()
    config = load_config()
    exchange_handler = ExchangeHandler(config)
    payment_handler = PaymentHandler(config)
    telegram_bot = TelegramBot(config)
    
    while True:
        try:
            # Example transaction data; replace with actual fetching logic
            transactions = [
                {'method': 'upi', 'amount_inr': 5000, 'bank': 'account1', 'exchange': 'binance'},
                {'method': 'debit_card', 'amount_inr': 10000, 'bank': 'account2', 'exchange': 'coinex'},
                {'method': 'imps', 'amount_inr': 15000, 'bank': 'account1', 'exchange': 'bybit'}
            ]
            
            for transaction in transactions:
                success = payment_handler.process_payment(
                    payment_method=transaction['method'],
                    amount_inr=transaction['amount_inr'],
                    exchange_name=transaction['exchange'],
                    bank_account_name=transaction['bank']
                )
                if success:
                    exchange_handler.buy_usdt(transaction['exchange'], transaction['amount_inr'])
                    telegram_bot.send_message(f"Processed payment and bought USDT on {transaction['exchange']} for {transaction['amount_inr']} INR.")
            
            # Generate and send transaction summary as PDF
            telegram_bot.send_pdf(transactions)

            logging.info("Sleeping for a while before checking for new transactions...")
            time.sleep(config['sleep_interval'])
        
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            time.sleep(60)

if __name__ == '__main__':
    main()
