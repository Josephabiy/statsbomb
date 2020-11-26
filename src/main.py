import logging
import utils
import my_sql
from sql_vars import (
    TRUNCATE_TMP_QUERY,
    NULLS_TO_BADROWS_QUERY,
    COUNT_UPSERT_BADROWS_QUERY,
    REMOVE_NULLS_QUERY,
)
from config import (
    TAXI_ETL_TASKS,
    USER,
    PASSWORD,
    TMP_DB,
    PROD_DB,
    PORT,
    START_DATE,
    END_DATE,
)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    execution_dates = utils.date_range_by_month(START_DATE, END_DATE)
    for execution_date in execution_dates:

        for task in TAXI_ETL_TASKS:
            csv_url = task["csv_url"]
            table = task["name"]
            production_upsert_query = task["production_upsert_query"]
            schema = task["schema"]
            columns = [*schema]

            logging.info(f" Executing pipeline: '{table}' for date '{execution_date}'")

            logging.info(" Truncating tmp table to load")
            my_sql.execute_query(
                TRUNCATE_TMP_QUERY.format(db=TMP_DB, table=table),
                USER,
                PASSWORD,
                TMP_DB,
            )

            utils.s3_to_db(
                csv_url,
                execution_date,
                schema,
                table,
                USER,
                PASSWORD,
                PORT,
                TMP_DB,
            )

            not_null_columns = utils.not_null_columns(columns, table)

            logging.info(f" Writing Null rows to 'badrows.{table}'")
            my_sql.execute_query(
                NULLS_TO_BADROWS_QUERY.format(
                    table=table, db=TMP_DB, columns=not_null_columns
                ),
                USER,
                PASSWORD,
                TMP_DB,
            )

            logging.info(f" Count Null rows and write to 'badrows.dropped_rows'")
            my_sql.execute_query(
                COUNT_UPSERT_BADROWS_QUERY.format(
                    name=table, csv_date=execution_date, columns=not_null_columns
                ),
                USER,
                PASSWORD,
                TMP_DB,
            )

            logging.info(f" Removing Null rows from 'tmp.{table}")
            my_sql.execute_query(
                REMOVE_NULLS_QUERY.format(
                    table=table, db=TMP_DB, columns=not_null_columns
                ),
                USER,
                PASSWORD,
                TMP_DB,
            )

            logging.info(f" Upserting from tmp table {PROD_DB}.{table}")
            my_sql.execute_query(production_upsert_query, USER, PASSWORD, PROD_DB)
