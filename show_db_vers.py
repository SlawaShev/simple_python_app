#!/usr/bin/python3

import http.server
import socketserver
import MySQLdb

#open database connection
db = MySQLdb.connect("app_db","dbadmin","password","app_db")

#prepare cursor object using cursor() method
cursor = db.cursor()

#execute SQL query using execute() method
cursor.execute("SELECT VERSION()")

#fetch a single raw using fetchone() method
data = cursor.fetchone()
print("Database version : " + str(data))

#disconnect from server
db.close()
