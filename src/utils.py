import csv
import requests
import logging
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from tempfile import NamedTemporaryFile
from src import my_sql


def date_range_by_month(start_y_m, end_y_m):
    """
    Returns a list of dates 'yyyy-mm' for a given date range

    Args:
        start_y_m (str): start date 'yyyy-mm' format
        end_y_m (str): end date 'yyyy-mm' format
    Return:
        date_range (list): returns a list dates
    """
    start_date = datetime.strptime(start_y_m, "%Y-%m")
    end_date = datetime.strptime(end_y_m, "%Y-%m")

    date_range = []
    while start_date <= end_date:
        date_range.append(start_date.strftime("%Y-%m"))
        start_date += relativedelta(months=1)
    return date_range


def rows_to_csv(tempfile, rows):
    """
    Writes a list of rows to CSV tempfile

    Args:
        tempfile (tempfile): temporary file
        rows (rows): list of rows
    """
    writer = csv.writer(tempfile)
    writer.writerows(rows)
    tempfile.flush()


def not_null_columns(columns, nulls, table):
    """
    Joins not null columns from a table

    Args:
        columns (list): list of table columns
        nulls (list): list of columns which can contain nulls
        table (str): name of table
    Return:
        not_null_columns (str): joined not null columns
    """

    try:
        [columns.remove(null) for null in nulls]
        not_null_columns = ",".join(columns)
        return not_null_columns

    except Exception as e:
        logging.info(
            f"An error '{e}' has occurred whilst removing null column for '{table}'"
        )
        not_null_columns = ",".join(columns)
        return not_null_columns


def csv_date_append(rows, execution_date):
    """
    Inserts the execution date to a list of rows as the first element

    Args:
        rows (rows): list of rows
        execution_date (str): execution date 'yyyy-mm' format
    Return:
        rows (rows): list of rows
    """
    [row.insert(0, execution_date) for row in rows]
    return rows


def chunk_to_rows(chunk, execution_date):
    """
    Converts chunk to list, removes header and appends csv_date to row

    Args:
        chunk (rows): list of rows
        execution_date (str): execution date 'yyyy-mm' format
    Return:
        rows (rows): list of rows
    """
    url_content = chunk.decode("utf-8").split("\n")
    rows = [(row.strip()).split(",") for row in url_content]
    rows = rows[1:]
    rows = csv_date_append(rows, execution_date)
    return rows


def create_and_clean_dataframe(csvfile, schema):
    """
    Creates pandas dataframe from csv and applies transformation based on the supplied schema

    Args:
        tempfile (tempfile): temporary file
        schema (dict): schema of table columns
    Return:
        dataframe (dataframe): transformed pandas dataframe
    """
    dataframe = pd.read_csv(
        csvfile.name,
        sep=",",
        names=[*schema],
        low_memory=False,
        error_bad_lines=False,
        warn_bad_lines=True,
    )

    numeric_cols = [column for column, dtype in schema.items() if dtype == "numeric"]
    dataframe[numeric_cols] = dataframe[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    )

    return dataframe


def s3_to_db(csv_url, execution_date, schema, table, user, password, port, db):
    """
    Ingests raw file from S3 in chunks of 100MB, applies transformation and returns rows.
        Rows are written to temp file and appended to the relevant tmp table.

    Args:
        csv_url (url): S3 URL to raw file
        execution_date (str): execution date 'yyyy-mm' format
        schema (dict): schema of table columns
        table (str): name of table
        user (str): User name
        password (str): Password
        port (str): Port
        db (str): Database
    """
    try:
        with requests.get(csv_url.format(year_month=execution_date), stream=True) as r:

            for chunk in r.iter_content(chunk_size=100000000):
                rows = chunk_to_rows(chunk, execution_date)

                try:
                    with NamedTemporaryFile("w", suffix=".csv") as csvfile:
                        rows_to_csv(csvfile, rows)

                        logging.info(" Reading CSV to pandas dataframe")
                        dataframe = create_and_clean_dataframe(csvfile, schema)

                        logging.info(f" Loading dataframe chunk to 'tmp.{table}")
                        my_sql.dataframe_to_db(
                            dataframe,
                            user,
                            password,
                            port,
                            db,
                            table,
                        )

                except Exception as e:
                    logging.info(
                        f"An error '{e}' has occurred whilst loading chunk to DB"
                    )
    except Exception as e:
        logging.info(f"An error '{e}' has occurred whilst pulling '{csv_url}' from S3")
