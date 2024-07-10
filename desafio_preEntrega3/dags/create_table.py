# from sqlalchemy import create_engine
# from parameters import REDSHIFT_USERNAME, REDSHIFT_PASSWORD, REDSHIFT_HOST, REDSHIFT_DB, REDSHIFT_PORT, REDSHIFT_TABLE

# def create_table():
#     try:
#         conn_str = f'postgresql+psycopg2://{REDSHIFT_USERNAME}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}'
#         engine = create_engine(conn_str)

#         create_table_query = f"""
#         CREATE TABLE IF NOT EXISTS {REDSHIFT_TABLE}(
#             PRIMARY KEY (date, currency),
#             currency VARCHAR,
#             rate VARCHAR,
#             base VARCHAR,
#             date DATE,
#             timestamp TIMESTAMP,
#             ingestion_time TIMESTAMP
#             );
#         """

#         with engine.connect() as connection:
#             connection.execute(create_table_query)
#         print("Tabla creada exitosamente en Redshift")
#     except Exception as e:
#         print(f"Error al crear la tabla en Redshift: {e}")

from sqlalchemy import create_engine, text
from sqlalchemy.exc import ProgrammingError
from parameters import REDSHIFT_USERNAME, REDSHIFT_PASSWORD, REDSHIFT_HOST, REDSHIFT_DB, REDSHIFT_PORT, REDSHIFT_TABLE

def create_table():
    try:
        conn_str = f'postgresql+psycopg2://{REDSHIFT_USERNAME}:{REDSHIFT_PASSWORD}@{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}'
        engine = create_engine(conn_str)

        create_table_query = f"""
        CREATE TABLE IF NOT EXISTS {REDSHIFT_TABLE} (
            currency VARCHAR,
            rate FLOAT,
            base VARCHAR,
            date DATE,
            timestamp TIMESTAMP,
            ingestion_time TIMESTAMP            
        )
        """

        with engine.connect() as connection:
            # Use sqlalchemy.text to execute raw SQL safely
            connection.execute(text(create_table_query))
        
        print("Tabla creada exitosamente en Redshift")
    except ProgrammingError as pe:
        print(f"Error de programación al crear la tabla en Redshift: {pe}")
    except Exception as e:
        print(f"Error al crear la tabla en Redshift: {e}")

if __name__ == "__main__":
    create_table()
