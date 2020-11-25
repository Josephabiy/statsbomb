import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta


def date_range_by_month(start_y_m, end_y_m):
    start_date = datetime.strptime(start_y_m, "%Y-%m")
    end_date = datetime.strptime(end_y_m, "%Y-%m")

    date_range = []
    while start_date <= end_date:
        date_range.append(start_date.strftime("%Y-%m"))
        start_date += relativedelta(months=1)
    return date_range


def rows_to_csv(tempfile, rows):
    writer = csv.writer(tempfile)
    writer.writerows(rows)
    tempfile.flush()


def not_null_columns(columns, table):
    if table == "hv_for_hire":
        not_null_columns = ",".join(columns[:-1])
    else:
        not_null_columns = ",".join(columns)
    return not_null_columns


def csv_date_append(rows, execution_date):
    [row.insert(0, execution_date) for row in rows]
    return rows
