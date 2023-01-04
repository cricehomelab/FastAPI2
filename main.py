import logging
import database
import os
import ingest



DATABASE_NAME ="database"
DIRECTORY = os.getcwd()
DATABASE_PATH = f"{DIRECTORY}/{DATABASE_NAME}.db"

def main():
    create_logging()
    logging.info("Starting...")
    logging.info("Creating connection")
    engine = database.create_connection(DATABASE_NAME)
    logging.info("Creating tables if they do not exist.")
    if not os.path.isfile(DATABASE_PATH):
        logging.info(f"{DATABASE_PATH} not found creating file.")
        database.create_table(engine)
    else:
        logging.info(f"{DATABASE_PATH} already exists.")
    logging.info("adding some data to the table.")
    complete = database.add_data(engine, ingest.list)
    logging.info(f"Was data added?: {complete}")

def create_logging():
    """sets up and configures logging."""
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)



if __name__ == '__main__':
    main()