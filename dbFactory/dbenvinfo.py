import os
from dataclasses import dataclass

''' Reads in from Environment variables
    DB_DIALECT,
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_DBNAME
    Just create dataclass after load_dotenv()
    and give to Database as dbinfo.'''
@dataclass
class DBInfo:
    def __init__(self):
        self.db_dialect = os.getenv('DB_DIALECT')
        self.db_username = os.getenv('DB_USERNAME')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_host = os.getenv('DB_HOST')
        self.db_port = os.getenv('DB_PORT')
        self.db_name = os.getenv('DB_NAME')
