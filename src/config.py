import sql_vars

TAXI_ETL_TASKS = [
    {
        "name": "yellow_taxi",
        "csv_url": "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_{year_month}.csv",
        "tmp_upsert_query": sql_vars.INSERT_INTO_YELLOW_TAXI_TMP,
        "production_upsert_query": sql_vars.YELLOW_TAXI_UPSERT_QUERY,
        "schema": {
            "csv_date" : "string",
            "VendorID": "numeric",
            "tpep_pickup_datetime": "string",
            "tpep_dropoff_datetime": "string",
            "passenger_count": "numeric",
            "trip_distance": "numeric",
            "RatecodeID": "numeric",
            "store_and_fwd_flag": "string",
            "PULocationID": "numeric",
            "DOLocationID": "numeric",
            "payment_type" :"numeric",
            "fare_amount": "numeric",
            "extra": "numeric",
            "mta_tax": "numeric",
            "tip_amount":"numeric",
            "tolls_amount" :"numeric",
            "improvement_surcharge": "numeric",
            "total_amount": "numeric",
            "congestion_surcharge": "numeric",
        },
    },
    {
        "name": "green_taxi",
        "csv_url": "https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_{year_month}.csv",
        "tmp_upsert_query": sql_vars.INSERT_INTO_GREEN_TAXI_TMP,
        "production_upsert_query": sql_vars.GREEN_TAXI_UPSERT_QUERY,
        "schema": {
            "csv_date": "string",
            "VendorID": "numeric",
            "lpep_pickup_datetime": "string",
            "lpep_dropoff_datetime": "string",
            "store_and_fwd_flag": "string",
            "RatecodeID": "numeric",
            "PULocationID": "numeric",
            "DOLocationID": "numeric",
            "passenger_count": "numeric",
            "trip_distance": "numeric",
            "fare_amount": "numeric",
            "extra": "numeric",
            "mta_tax": "numeric",
            "tip_amount": "numeric",
            "tolls_amount": "numeric",
            "ehail_fee": "numeric",
            "improvement_surcharge": "numeric",
            "total_amount": "numeric",
            "payment_type": "numeric",
            "trip_type": "numeric",
            "congestion_surcharge": "numeric",
        },
    },
    {
        "name": "for_hire",
        "csv_url": "https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year_month}.csv",
        "tmp_upsert_query": sql_vars.INSERT_INTO_FOR_HIRE_TAXI_TMP,
        "production_upsert_query": sql_vars.FOR_HIRE_TAXI_UPSERT_QUERY,
        "schema": {
            "csv_date": "string",
            "dispatching_base_num": "string",
            "pickup_datetime": "string",
            "dropoff_datetime": "string",
            "PULocationID": "numeric",
            "DOLocationID": "numeric",
            "SR_Flag": "numeric",
        },
    },
    {
        "name": "hv_for_hire",
        "csv_url": "https://nyc-tlc.s3.amazonaws.com/trip+data/fhvhv_tripdata_{year_month}.csv",
        "tmp_upsert_query": sql_vars.INSERT_INTO_HV_FOR_HIRE_TAXI_TMP,
        "production_upsert_query": sql_vars.HIGH_VOLUME_FOR_HIRE_TAXI_UPSERT_QUERY,
        "schema": {
            "csv_date": "string",
            "hvfhs_license_num": "string",
            "dispatching_base_num": "string",
            "pickup_datetime": "string",
            "dropoff_datetime": "string",
            "PULocationID": "numeric",
            "DOLocationID": "numeric",
            "SR_Flag": "numeric"
        },
    },
]

# DATE RANGE YEAR-MONTH
START_DATE = "2018-01"
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
