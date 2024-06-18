from modules.data_from_api import exchange_rate_data

def extract_data(api_url):
    data = exchange_rate_data(api_url)
    return data
