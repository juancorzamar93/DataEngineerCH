
CREATE TABLE exchange_rate_data(
            PRIMARY KEY (date, currency),
            currency VARCHAR,
            rate FLOAT,
            base VARCHAR,
            date DATE,
            timestamp TIMESTAMP,
            ingestion_time TIMESTAMP            
        );