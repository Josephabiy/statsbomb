import logging
import utils
import my_sql
from config import (
    TAXI_ETL_TASK as task,
    USER,
    PASSWORD,
    TMP_DB,
    PORT,
    START_DATE,
    END_DATE,
)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    execution_dates = utils.date_range_by_month(START_DATE, END_DATE)
    for execution_date in execution_dates:

        csv_url = task["csv_url"]
        table = task["name"]
        production_upsert_query = task["production_upsert_query"]
        schema = task["schema"]
        nulls = task["nulls"]
        columns = [*schema]
        not_null_columns = utils.not_null_columns(columns, nulls, table)

        logging.info(f" Executing pipeline: '{table}' for date '{execution_date}'")

        utils.s3_to_db(
            csv_url,
            execution_date,
            schema,
            not_null_columns,
            table,
            USER,
            PASSWORD,
            PORT,
            TMP_DB,
            production_upsert_query,
        )
