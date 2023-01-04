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
                                (id primary key,
                                 name text,
                                 age int)
                               """
    with engine.connect() as conn:
        conn.execute(text(sql_create_table_command))
        conn.commit()
    
