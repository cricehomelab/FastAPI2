from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData, insert
from sqlalchemy.orm import registry, relationship, declarative_base

mapper_registry = registry()
Base = declarative_base()


class Person(Base):
    __tablename__  = "some_table"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer)


def create_connection(name):
    """creates connection to database. Returns that connection."""
    engine = create_engine(f"sqlite+pysqlite:///{name}.db", echo=True, future=True)
    return engine

def create_table(engine):
    """Creates the table for the database."""

    metadata_obj = MetaData()

    new_table = Table(
        "some_table",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("age", Integer),
    )
    metadata_obj.create_all(engine)
    return new_table

def add_data(engine, metadata_obj, data):
    """Adds data to table with current schema"""
    
    for num, person in enumerate(data):
        people = insert(metadata_obj).values(name=person["name"], age=person["age"])
        with engine.connect() as conn:
            conn.execute(people)
            conn.commit()


    '''
    sql_insert_command = """INSERT INTO 
                                some_table (name, age) 
                            VALUES 
                                (:name, :age)"""
    with engine.connect() as conn:        
        conn.execute(text(sql_insert_command), data) # adds values to table.
        conn.commit() # Commits values to db.
        return True
    '''

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


