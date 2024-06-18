SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'juanzamar93_coderhouse';

DROP TABLE IF EXISTS juanzamar93_coderhouse.stage_yfinance_google;

CREATE TABLE stage_yfinance_google(
	specific_area	VARCHAR(200)
,   stock_actions   VARCHAR(50)
,   revenue         VARCHAR(50)
,   value           VARCHAR(50)
,   avg_data        VARCHAR(50)
,   date_to_stage      DATE
);

SELECT
*
FROM juanzamar93_coderhouse.stage_yfinance_google ;

