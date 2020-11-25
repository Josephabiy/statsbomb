import pymysql
from sqlalchemy import create_engine


def connect_to_db(user, password, db):
    """
    Creates a connection to MySql database

    Args:
        user (str): User name
        password (str): Password
        db (str): Database
    Return:
        con (connection object)
    """
    con = pymysql.connect(
        user=user,
        password=password,
        db=db,
    )
    return con


def execute_query(query, user, password, db):
    """
    Executes a query against MySql database

    Args:
        query (sql): MySql query
        user (str): User name
        password (str): Password
        db (str): Database
    """
    con = connect_to_db(user, password, db)

    try:
        with con.cursor() as cursor:
            cursor.execute(query)
        con.commit()
    finally:
        con.close()


def dataframe_to_db(dataframe, user, password, port, db, table):
    """
    Loads Pandas Dataframe to MySql database in chunks of 100,000 rows

    Args:
        dataframe (dataframe): Pandas dataframe
        user (str): User name
        password (str): Password
        port (str): Port
        db (str): Database
        table (str): MySql table
    """
    engine = create_engine(f"mysql+pymysql://{user}:{password}@:{port}/{db}")
    dataframe.to_sql(
        name=table,
        con=engine,
        if_exists="append",
        index=False,
        chunksize=100000,
    )
