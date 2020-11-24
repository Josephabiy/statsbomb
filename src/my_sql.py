import pymysql
from sqlalchemy import create_engine


def connect_to_db(user, password, db):
    con = pymysql.connect(
        user=user,
        password=password,
        db=db,
    )
    return con


def execute_query(query, user, password, db):
    con = connect_to_db(user, password, db)

    try:
        with con.cursor() as cursor:
            cursor.execute(query)
        con.commit()
    finally:
        con.close()


def dataframe_to_db(dataframe, user, password, port, db, table):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@:{port}/{db}")
    dataframe.to_sql(
        name=table,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=100000,
    )
