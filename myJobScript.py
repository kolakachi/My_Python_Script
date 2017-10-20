from dbOperations import *

from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


#set the API to read only and open
Jenkins_API = open("jobs.xml","r")

#get the cotents of the API
contents = Jenkins_API.read()

#parse the API with Beautiful soup
soup = BeautifulSoup(contents, 'xml')

#find and get all job names
JobNames = soup.find_all('name')

#find and get all job statuses
JobStatuses = soup.find_all('status')

#find and get all jobs
AvailableJobs = soup.find_all('job')

if tableExists('jobs'):
    for i in range(0, len(AvailableJobs)):
        name = str(JobNames[i].get_text())
        status = str(JobStatuses[i].get_text())
        timechecked =str(datetime.now())

        addToTableJobs(name, status, timechecked)
        print "Added entry"
else:
    createTableJobs()

    for i in range(0, len(AvailableJobs)):
        name = str(JobNames[i].get_text())
        status = str(JobStatuses[i].get_text())
        timechecked =str(datetime.now())

        addToTableJobs(name, status, timechecked)
        print "Created table and added entry"
    
    
    
