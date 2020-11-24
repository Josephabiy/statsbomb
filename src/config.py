import sql_vars

ETL_TASKS = [
    {
        "name": "yellow_taxi",
        "csv_url": "https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv",  # add date format {year_month}
        "production_upsert_query": sql_vars.YELLOW_TAXI_UPSERT_QUERY,
        "columns": [
            "VendorID",
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
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
        "pk_constraint": [
            "tpep_pickup_datetime",
            "tpep_dropoff_datetime",
            "PULocationID",
            "DOLocationID",
            "VendorID",
        ],
    },
    # {
    #     "name": "green_taxi",
    #     "csv_url": "https://s3.amazonaws.com/nyc-tlc/trip+data/green_tripdata_2020-01.csv",  # add date format {year_month}
    #     "columns": [
    #         "VendorID",
    #         "lpep_pickup_datetime",
    #         "lpep_dropoff_datetime",
    #         "store_and_fwd_flag",
    #         "RatecodeID",
    #         "PULocationID",
    #         "DOLocationID",
    #         "passenger_count",
    #         "trip_distance",
    #         "fare_amount",
    #         "extra",
    #         "mta_tax",
    #         "tip_amount",
    #         "tolls_amount",
    #         "ehail_fee",
    #         "improvement_surcharge",
    #         "total_amount",
    #         "payment_type",
    #         "trip_type",
    #         "congestion_surcharge",
    #     ],
    # },
    # {
    #     "name": "for_hire",
    #     "csv_url": "https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2020-01.csv",  # add date format {year_month}
    #     "columns": [
    #         "dispatching_base_num",
    #         "pickup_datetime",
    #         "dropoff_datetime",
    #         "PULocationID",
    #         "DOLocationID",
    #         "SR_Flag",
    #     ],
    # },
    # {
    #     "name": "hv_for_hire",
    #     "csv_url": "https://nyc-tlc.s3.amazonaws.com/trip+data/fhvhv_tripdata_2020-01.csv",  # add date format {year_month}
    #     "columns": [
    #         "hvfhs_license_num",
    #         "dispatching_base_num",
    #         "pickup_datetime",
    #         "dropoff_datetime",
    #         "PULocationID",
    #         "DOLocationID",
    #         "SR_Flag",
    #     ],
    # },
]

# DATE RANGE YEAR-MONTH
DATE_RANGE = ""

# MYSQL CONN
HOST = "%"
USER = "newuser"
PASSWORD = "Taxitask@stats"
TMP_DB = "tmp"
PROD_DB = "trips"
PORT = 3306
