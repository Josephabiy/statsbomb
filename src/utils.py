import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta


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

    elif table =="yellow_taxi":
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
