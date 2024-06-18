
from dotenv import load_dotenv
import os

load_dotenv()

BASE = 'ARS'
SYMBOLS = 'EUR,USD,CNY'
API_URL = f'https://api.apilayer.com/exchangerates_data/latest?symbols={SYMBOLS}&base={BASE}'

# Redshift credentials
REDSHIFT_USERNAME = os.getenv('REDSHIFT_USERNAME')
REDSHIFT_PASSWORD = os.getenv('REDSHIFT_PASSWORD')
REDSHIFT_HOST = os.getenv('REDSHIFT_HOST')
REDSHIFT_DB = os.getenv('REDSHIFT_DB')
REDSHIFT_PORT = os.getenv('REDSHIFT_PORT')
REDSHIFT_TABLE = 'exchange_rate_data'
API_KEY = os.getenv('API_KEY')
