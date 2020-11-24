import csv


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
