"""  """
import logging
import pandas as pd
import aws
import utils
from my_sql import execute_query, dataframe_to_db
from sql_vars import TRUNCATE_TMP_QUERY, NULLS_TO_BADROWS_QUERY, REMOVE_NULLS_QUERY
from config import ETL_TASKS, USER, PASSWORD, TMP_DB, PROD_DB, PORT
from tempfile import NamedTemporaryFile

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    
    for task in ETL_TASKS:
        csv_url = task["csv_url"]
        table = task["name"]
        production_upsert_query = task["production_upsert_query"]
        columns = task["columns"]
        pk_constraint = task["pk_constraint"]

        with NamedTemporaryFile("w", suffix=".csv") as csvfile:

            rows = aws.pull(csv_url)

            utils.rows_to_csv(csvfile, rows)

            logging.info("Reading CSV to pandas dataframe")
            dataframe = pd.read_csv(
                csvfile.name, sep=",", names=columns, low_memory=False
            )

            logging.info("Truncating tmp table to prepare dataframe load")
            execute_query(
                TRUNCATE_TMP_QUERY.format(db=TMP_DB, table=table),
                USER,
                PASSWORD,
                TMP_DB,
            )

            logging.info("Loading dataframe to tmp table")
            dataframe_to_db(
                dataframe,
                USER,
                PASSWORD,
                PORT,
                TMP_DB,
                table,
            )

        not_null_columns = utils.not_null_columns(columns, table)

        logging.info("Writing Null rows to badrows table")
        execute_query(
            NULLS_TO_BADROWS_QUERY.format(
                table=table, db=TMP_DB, columns=not_null_columns
            ),
            USER,
            PASSWORD,
            TMP_DB,
        )

        logging.info("Removing Null rows from tmp table")
        execute_query(
            REMOVE_NULLS_QUERY.format(table=table, db=TMP_DB, columns=not_null_columns),
            USER,
            PASSWORD,
            TMP_DB,
        )

        logging.info("Upserting tmp table to production")
        execute_query(production_upsert_query, USER, PASSWORD, PROD_DB)
