# def extract_data():
#     headers = {"apikey": API_KEY}
#     try:
#         response = requests.get(API_URL, headers=headers)
#         response.raise_for_status()
#         return response.json()
#     except requests.RequestException as e:
#         print(f"Error al realizar la solicitud a la API: {e}")
#         return None

from modules.data_from_api import exchange_rate_data

def extract_data(api_url):
    data = exchange_rate_data(api_url)
    return data
