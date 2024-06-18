# import os
# from modules.load_data import load_data
# from modules.data_transformation import transform_data
# from modules.data_from_api import exchange_rate_data
# from module.extract_data import extract_data
# from module.create_table import create_table
# from module.validate_credentials import validate_credentials
# from parameters import url
# from dotenv import load_dotenv
# import pandas as pd

# load_dotenv()


# def main():
#     if not validate_credentials():
#         return

#     create_table()
#     data = extract_data()
#     if data:
#         transformed_data = transform_data(data)
#         if transformed_data is not None:
#             load_data(transformed_data)

# if __name__ == '__main__':
#     main()
    
from modules.load_data import load_data
from modules.data_transformation import transform_data
from modules.extract_data import extract_data
from modules.create_table import create_table
from modules.validate_credentials import validate_credentials
from parameters import API_URL
from dotenv import load_dotenv

load_dotenv()

def main():
    if not validate_credentials():
        return

    create_table()
    data = extract_data(API_URL)
    if data:
        transformed_data = transform_data(data)
        if transformed_data is not None:
            load_data(transformed_data)

if __name__ == '__main__':
    main()
