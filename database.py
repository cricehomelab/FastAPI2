from sqlalchemy import create_engine, text



def create_connection(name):
    """creates connection to database. Returns that connection."""
    engine = create_engine(f"sqlite+pysqlite:///{name}.db", echo=True, future=True)
    return engine

def create_table(engine):
    """Creates the table for the database."""
    sql_create_table_command = """
                               CREATE TABLE 
                                   some_table
                                (id integer PRIMARY KEY,
                                 name text,
                                 age integer)
                               """
    with engine.connect() as conn:
        conn.execute(text(sql_create_table_command))
        conn.commit()

def add_data(engine, data):
    sql_insert_command = """INSERT INTO 
                                some_table (name, age) 
                            VALUES 
                                (:name, :age)"""
    with engine.connect() as conn:
        conn.execute(text(sql_insert_command), data) # adds values to table.
        conn.commit() # Commits values to db.
        return True
    return False
