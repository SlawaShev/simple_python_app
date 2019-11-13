#!/usr/bin/python3

import MySQLdb
from http.server import BaseHTTPRequestHandler, HTTPServer
 
app_server_ipv4 = "127.0.0.1" 
app_server_port = "8080"
app_db_ipv4 = "127.0.0.1"

db = MySQLdb.connect(app_db_ipv4,"dbadmin","password","app_ad" )
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE USERS (
         ID  INT NOT NULL,
         FIRST_NAME CHAR(20),
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         EMAIL CHAR(20),
         EMAIL STATUS CHAR(1))"""

cursor.execute(sql)


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # POST
    #def do_POST(self):


    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        print("We are in handler. Protocol version = " + self.protocol_version)
        print("Client address " + str(self.client_address))
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
    print('starting server...')
 
    # Server settings
    # Choose port 8081 and specify app_server's ip address
    server_address = (app_server_ipv4, int(app_server_port))

    # Create instance of HTTPServer with http server settings (first argument and my RequestHandler 
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

    print('running server...')
    httpd.serve_forever()
 
 
run()


