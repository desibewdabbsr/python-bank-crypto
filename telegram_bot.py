import telegram
import logging
from utils.pdf_generator.py import generate_pdf

class TelegramBot:
    def __init__(self, config):
        self.bot = telegram.Bot(token=config['telegram']['bot_token'])
        self.chat_id = config['telegram']['chat_id']

    def send_message(self, message):
        try:
            self.bot.send_message(chat_id=self.chat_id, text=message)
            logging.info(f"Sent message to Telegram: {message}")
        except Exception as e:
            logging.error(f"Failed to send message to Telegram. Error: {e}")

    def send_pdf(self, transactions):
        filename = "transactions.pdf"
        generate_pdf(transactions, filename)
        try:
            with open(filename, 'rb') as pdf_file:
                self.bot.send_document(chat_id=self.chat_id, document=pdf_file)
            logging.info("Sent PDF file to Telegram.")
        except Exception as e:
            logging.error(f"Failed to send PDF file to Telegram. Error: {e}")
