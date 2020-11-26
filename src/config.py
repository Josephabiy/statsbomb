import sql_vars

TAXI_ETL_TASK = {
    "name": "yellow_taxi",
    "csv_url": "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_{year_month}.csv",
    "production_upsert_query": sql_vars.YELLOW_TAXI_UPSERT_QUERY,
    "schema": {
        "csv_date": "string",
        "VendorID": "numeric",
        "tpep_pickup_datetime": "string",
        "tpep_dropoff_datetime": "string",
        "passenger_count": "numeric",
        "trip_distance": "numeric",
        "RatecodeID": "numeric",
        "store_and_fwd_flag": "string",
        "PULocationID": "numeric",
        "DOLocationID": "numeric",
        "payment_type": "numeric",
        "fare_amount": "numeric",
        "extra": "numeric",
        "mta_tax": "numeric",
        "tip_amount": "numeric",
        "tolls_amount": "numeric",
        "improvement_surcharge": "numeric",
        "total_amount": "numeric",
        "congestion_surcharge": "numeric",
    },
    "nulls": [
        "VendorID",
        "passenger_count",
        "trip_distance",
        "RatecodeID",
        "store_and_fwd_flag",
        "PULocationID",
        "DOLocationID",
        "payment_type",
        "fare_amount",
        "extra",
        "mta_tax",
        "tip_amount",
        "tolls_amount",
        "improvement_surcharge",
        "total_amount",
        "congestion_surcharge",
    ],
}

# DATE RANGE YEAR-MONTH
START_DATE = "2010-06"
END_DATE = "2020-06"

# mysql con
HOST = "%"
USER = "remoteuser"
PASSWORD = "Taxitask@stats"
TMP_DB = "tmp"
PROD_DB = "trips"
PORT = 3306

# original local
# HOST = "%"
# USER = "newuser"
# PASSWORD = "Taxitask@stats"
# TMP_DB = "tmp"
# PROD_DB = "trips"
# PORT = 3306
