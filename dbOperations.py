import sqlite3

#connect to database
connection = sqlite3.connect('jobs.db')
cursor = connection.cursor()

#create new table
def createTableJobs():
    cursor.execute('''CREATE TABLE jobs(id INT PRIMRK KEY, jobname TEXT, jobstatus TEXT, lastchecked TEXT)''')

#check if table exist
def tableExists(tableName):
    statement ="SELECT name FROM sqlite_master WHERE type='table';"
    if (tableName,) in cursor.execute(statement).fetchall():
        return True
    else:
        return False

#make entries to table
def addToTableJobs(name, status, timechecked):
    cursor.execute('''INSERT INTO jobs(jobname, jobstatus, lastchecked) VALUES(?,?,?)''',(name, status, timechecked))
    
    
