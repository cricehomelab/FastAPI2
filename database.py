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
    """Adds data to table with current schema"""
    sql_insert_command = """INSERT INTO 
                                some_table (name, age) 
                            VALUES 
                                (:name, :age)"""
    with engine.connect() as conn:
        conn.execute(text(sql_insert_command), data) # adds values to table.
        conn.commit() # Commits values to db.
        return True

def of_age_user(engine, age):
    """checks if user is greater than or equal to specified age."""
    sql_query_command = f"""
                        SELECT
                            name
                        FROM
                            some_table
                        WHERE
                            age >= :age
                        """
    with engine.connect() as conn:
        print(conn)
        results = conn.execute(text(sql_query_command), {"age": age})
        names = []
        for name in results:
            names.append(name)
        return names

