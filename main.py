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

def myproc(sess, str1=None, str2=None):
    print(str1, str2, sess)

def someproc(proc):
    proc(sess='Six')

def otherproc(sess):
    myproc(sess=sess, str1='One', str2='Two')
#l = lambda str : myproc(str1='One', str2='Two', str3=str) 

someproc(otherproc)
print(db.get_tables())