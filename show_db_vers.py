#!/usr/bin/python

import MySQLdb

#open database connection
db = MySQLdb.connect("localhost","demouser","demopassword","firstDB")

#prepare cursor object using cursor() method
cursor = db.cursor()

#execute SQL query using execute() method
cursor.execute("SELECT VERSION()")

#fetch a single raw using fetchone() method
data = cursor.fetchone()
print "Database version : %s " % data

#disconnect from server
db.close()
