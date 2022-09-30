import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .dbenvinfo import DBInfo

''' Database class
    that handles the sqlalchemy engine, session, and declarative_base
    using the supplied database information
    or DBInfo.'''
class Database:
    ''' Supply the full database infomation
        or give it DBInfo object that contains the database info '''
    def __init__( self, dialect: str=None, username: str=None, password: str=None, host: str=None, port: str=None, db_name: str=None, dbinfo: DBInfo=None ):
        if dbinfo is not None:
            self.dialect = dbinfo.db_dialect
            self.username = dbinfo.db_username
            self.password = dbinfo.db_password
            self.host = dbinfo.db_host
            self.port = dbinfo.db_port
            self.db_name = dbinfo.db_name
        else:
            self.dialect = dialect
            self.username = username
            self.password = password
            self.host = host
            self.port = port
            self.db_name = db_name

        self.__engine = create_engine( self.get_url() )
        self.__Session = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.__Base = declarative_base()

    ''''''
    def get_url(self):
        url = f"{self.dialect}://{self.username}:{urllib.parse.quote(self.password.encode('utf8'))}@{self.host}:{self.port}/{self.db_name}"
        return url

    ''' Gets the Session.'''
    def get_Session(self):
        return self.__Session()

    ''' Gets the declarative_base'''
    def get_Base(self):
        return self.__Base
    
    ''' Runs session_proc(session) with a session
        that is opened and closed
        automatically.
        Returns what proc returns.'''
    def run_session(self, session_proc):
        with self.get_Session() as session:
            return session_proc(session)

    def get_tables(self):
        return self.__engine.table_names()

    ''''''
    def __str__(self):
        return self.get_url()
    