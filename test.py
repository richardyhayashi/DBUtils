from config.settings import Settings
from dbFactory.db import Database

# Get the environment settings.
settings = Settings()

print(settings.dict())

# Initialize the database with settings.
db = Database(settings=settings)

print(db)
print(repr(db))

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