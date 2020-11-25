import csv
import requests
import logging
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
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


def not_null_columns(columns, table):
    """
    Joins not null columns from a table

    Args:
        columns (list): list of table columns
        table (str): name of table
    Return:
        not_null_columns (str): joined not null columns
    """
    if table == "for_hire":
        columns.remove("SR_Flag")
        not_null_columns = ",".join(columns)

    elif table == "hv_for_hire":
        columns.remove("SR_Flag")
        not_null_columns = ",".join(columns)

    elif table == "green_taxi":
        columns.remove("ehail_fee")
        not_null_columns = ",".join(columns)

    elif table == "yellow_taxi":
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


def s3_to_db(csv_url, execution_date, columns, table, user, password, port, db, query):
    """
    Ingests raw file from S3 in chunks of 10MB, applies transformation and returns rows.
        Rows are written converted to tuple and appended to the relevant tmp table.

    Args:
        csv_url (url): S3 URL to raw file
        execution_date (str): execution date 'yyyy-mm' format
        columns (list): list of table columns
        table (str): name of table
        user (str): User name
        password (str): Password
        port (str): Port
        db (str): Database
    """
    try:
        with requests.get(csv_url.format(year_month=execution_date), stream=True) as r:

            for chunk in r.iter_content(chunk_size=10000000):
                rows = chunk_to_rows(chunk, execution_date)

                logging.info(" Loading chunk to tmp table")
                for row in rows:
                    my_sql.execute_query(
                        query.format(values=tuple(row)),
                        user,
                        password,
                        db,
                    )

    except Exception as e:
        logging.info(
            f"An error '{e}' has occurred whilst pulling '{csv_url}' from S3 bucket"
        )
