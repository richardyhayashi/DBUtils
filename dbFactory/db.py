import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from .dbenvinfo import DBInfo
from config.settings import Settings

class Database:
    """ database class
    that handles the sqlalchemy engine and session
    using the supplied database information
    or info."""
    
    #def __init__(self, dialect=None, username=None, password=None, host=None, port=None, db_name=None, dbinfo: DBInfo=None ):
    def __init__(self, dialect=None, username=None, password=None, host=None, port=None, db_name=None, settings: Settings =None ):
        """ Supply the full database infomation
            or give it DBInfo object with database """
        #print(settings)
        #if dbinfo is not None:
        if settings is not None:
            #self.dialect = dbinfo.db_dialect
            #self.username = dbinfo.db_username
            #self.password = dbinfo.db_password
            #self.host = dbinfo.db_host
            #self.port = dbinfo.db_port
            #self.db_name = dbinfo.db_name
            self.dialect = settings.db_dialect
            self.username = settings.db_username
            self.password = settings.db_password
            self.host = settings.db_host
            self.port = settings.db_port
            self.db_name = settings.db_name
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

    def get_url(self) -> str:
        """"""
        url = f"{self.dialect}://{self.username}:{urllib.parse.quote(self.password.encode('utf8'))}@{self.host}:{self.port}/{self.db_name}"
        return url
    
    def get_session(self):
        """ Gets the session."""
        return self.__Session()

    def run_session(self, session_proc):
        """ Runs session_proc(session) with a session
        that is opened and closed
        automatically.
        Returns what proc returns."""
        with self.get_session() as session:
            return session_proc(session)

    def get_tables(self):
        return self.__engine.table_names()

    ''''''
    def __str__(self):
        return self.get_url()
    