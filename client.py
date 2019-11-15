#!/usr/bin/python3

from http.client import HTTPConnection
 
app_server_ipv4 = "app_server" 
app_server_port = "8080"
app_db_ipv4 = "app_db"

http_client = HTTPConnection(app_server_ipv4, int(app_server_port))
http_client.request("GET", "/")
response = http_client.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

if (response.status == 401):
    login = input("Enter your login ")
    password = input("Enter your password ")
#    http_client.putheader("Authorization", "ShevSlawa zxcvbn")
    http_client.request("GET", "/", None, {"Authorization": login + " " + password})
    
