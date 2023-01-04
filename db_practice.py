import sqlalchemy
from sqlalchemy import create_engine, text
import logging

# logging config setup.
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

# testing the logging.
# https://docs.sqlalchemy.org/en/14/tutorial/index.html#unified-tutorial
logging.info(f'DB Module starting....')
logging.info(f'SqlAlchemy version: {sqlalchemy.__version__}')



# https://docs.sqlalchemy.org/en/14/tutorial/engine.html

# Memory based DB creation.
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html

'''
# Does not commit to DB. 
with engine.connect() as conn:
    results = conn.execute(text("select 'hello world'"))
    logging.info(f'number of results in query: {len(results.all())}')
    for result in results.all():
        logging.info(result)
'''

# Commiting to to the DB. 
sql_create_table = "CREATE TABLE some_table (x int, y int)"
sql_insert_command = "INSERT INTO some_table (x, y) VALUES (:x, :y)"

'''
# Commented for other commands. 
with engine.connect() as conn:
    conn.execute(text(sql_create_table))
    conn.execute(text(sql_insert_command), [{"x": 1, "y": 1}, {"x": 2, "y": 4}],)
    conn.commit()
'''

list = [
    {"x": 1, "y": 1},
    {"x": 2, "y": 4},
    {"x": 3, "y": 7},
    {"x": 4, "y": 10},
    {"x": 5, "y": 13},
    {"x": 6, "y": 16},
    {"x": 7, "y": 19},
    {"x": 8, "y": 22},
    {"x": 10, "y": 28}
    ]

with engine.connect() as conn:
    conn.execute(text(sql_create_table)) # Creates the table in sql.
    conn.execute(text(sql_insert_command), list) # adds values to table.
    conn.commit() # Commits values to db. 

# Basic query.
sql_query_command = "SELECT x, y FROM some_table"

with engine.connect() as conn:
    results = conn.execute(text(sql_query_command)) # Running query on commited data. 
    for result in results:
        logging.info(result)


sql_query_command = """
                    SELECT
                        x,
                        y
                    FROM
                        some_table
                    WHERE
                        y > :y
                    ORDER BY
                        x ASC
                    """

with engine.connect() as conn:
    results = conn.execute(text(sql_query_command), {"y": 10})
    for result in results:
        logging.info(result)

sql_insert_command = """
                     INSERT INTO
                        some_table (x,y)
                     VALUES
                        (:x, :y)
                     """

list = [
        {"x": 9, "y": 25},
        {"x": 11, "y": 31},
        {"x": 12, "y": 34}
       ]

with engine.connect() as conn:
    conn.execute(text(sql_insert_command), list)
    conn.commit()

with engine.connect() as conn:
    results = conn.execute(text(sql_query_command), {"y": 10})
    for result in results:
        logging.info(result)



