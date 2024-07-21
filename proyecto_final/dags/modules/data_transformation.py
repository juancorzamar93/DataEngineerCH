import pandas as pd

def transform_data(data):
    try:
        rates = data.get('rates', {})
        timestamp = pd.to_datetime(data.get('timestamp'), unit='s')
        df = pd.DataFrame(rates.items(), columns=['currency', 'rate'])
        df['base'] = data.get('base')
        df['date'] = pd.to_datetime(data.get('date'), errors='coerce')  # Maneja fechas inválidas como NaT
        df['timestamp'] = timestamp
        df['ingestion_time'] = pd.Timestamp.now()
        return df
    except Exception as e:
        print(f"Error al transformar los datos: {e}")
        return None
    
def transform_bitmonedero_data(data):
    try:
        # Creando un DataFrame directamente con los datos necesarios
        df = pd.DataFrame({
            "buy_btc_ars": [data["buy_btc_ars"]],
            "sell_btc_ars": [data["sell_btc_ars"]],
            "updated_at_prices": [pd.to_datetime(data["updated_at_prices"])]
        })
        #df['ingestion_time'] = pd.Timestamp.now()  # Añade el tiempo de ingestión
        return df
    except Exception as e:
        print(f"Error al transformar datos de Bitmonedero: {e}")
        return None
