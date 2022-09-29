import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .dbenvinfo import DBInfo

''' database class
    that handles the sqlalchemy engine and session
    using the supplied database information
    or info.'''
class Database:
    ''' Supply the full database infomation
        or give it DBInfo object with database '''
    def __init__(self, dialect=None, username=None, password=None, host=None, port=None, db_name=None, dbinfo : DBInfo=None ):
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
        self.__Session = sessionmaker(bind=self.__engine)

    ''''''
    def get_url(self):
        url = f"{self.dialect}://{self.username}:{urllib.parse.quote(self.password.encode('utf8'))}@{self.host}:{self.port}/{self.db_name}"
        return url

    ''' Gets the session.'''
    def get_session(self):
        return self.__Session()

    ''' Runs session_proc(session) with a session
        that is opened and closed
        automatically.
        Returns what proc returns.'''
    def run_session(self, session_proc):
        with self.get_session() as session:
            return session_proc(session)

    ''''''
    def __str__(self):
        return self.get_url()
    