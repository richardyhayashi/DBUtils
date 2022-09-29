from os.path import join, dirname
from dotenv import load_dotenv
from dbFactory.db import Database
from dbFactory.dbenvinfo import DBInfo

dotenv_path = join(dirname(__file__), 'config', '.env')
load_dotenv( dotenv_path )

db = Database(dbinfo=DBInfo())

print( db )

proc = lambda session: print(session)
db.run_session(proc)
db.run_session(proc)
