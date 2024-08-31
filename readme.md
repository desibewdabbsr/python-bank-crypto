# project structure

python-bank-crypto/
│
├── config.yaml           # Configuration file for API keys, settings, etc.
├── main.py               # Main script to orchestrate the process
├── telegram_bot.py       # Telegram bot script to send notifications
├── utils/
│   ├── __init__.py       # Initialize utils package
│   ├── exchanges.py      # Functions to handle different exchange operations
│   ├── payments.py       # Functions to handle different payment methods
│   ├── logging_config.py # Custom logging setup
│   ├── pdf_generator.py  # Functions to generate PDFs of transactions
└── requirements.txt      # List of required Python packages



pip install -r requirements.txt


