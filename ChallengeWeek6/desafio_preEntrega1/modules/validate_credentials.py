# import os
# from dotenv import load_dotenv
# import pandas as pd

# load_dotenv()


# # Validar credenciales
# def validate_credentials():
#     credentials = {
#         "API_KEY": API_KEY,
#         "REDSHIFT_USERNAME": os.getenv('REDSHIFT_USERNAME'),
#         "REDSHIFT_PASSWORD": os.getenv('REDSHIFT_PASSWORD'),
#         "REDSHIFT_HOST": os.getenv('REDSHIFT_HOST').replace('http://', ''),
#         "REDSHIFT_DB": os.getenv('REDSHIFT_DB'),
#         "REDSHIFT_PORT": os.getenv('REDSHIFT_PORT')
#     }

#     for key, value in credentials.items():
#         if not value or value == '':
#             print(f"Error: {key} is not set properly.")
#             return False

#     print("All credentials are set properly:")
#     print(f"API_KEY: {'*' * len(API_KEY)}")
#     print(f"REDSHIFT_USERNAME: {'*' * len(REDSHIFT_USERNAME)}")
#     print(f"REDSHIFT_PASSWORD: {'*' * len(REDSHIFT_PASSWORD)}")
#     print(f"REDSHIFT_HOST: {REDSHIFT_HOST}")
#     print(f"REDSHIFT_DB: {REDSHIFT_DB}")
#     print(f"REDSHIFT_PORT: {REDSHIFT_PORT}")
#     return True


import os

def validate_credentials():
    credentials = {
        "API_KEY": os.getenv('API_KEY'),
        "REDSHIFT_USERNAME": os.getenv('REDSHIFT_USERNAME'),
        "REDSHIFT_PASSWORD": os.getenv('REDSHIFT_PASSWORD'),
        "REDSHIFT_HOST": os.getenv('REDSHIFT_HOST').replace('http://', ''),
        "REDSHIFT_DB": os.getenv('REDSHIFT_DB'),
        "REDSHIFT_PORT": os.getenv('REDSHIFT_PORT')
    }

    for key, value in credentials.items():
        if not value or value == '':
            print(f"Error: {key} is not set properly.")
            return False

    print("All credentials are set properly.")
    return True
