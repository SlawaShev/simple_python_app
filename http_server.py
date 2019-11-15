#!/usr/bin/python3

#import MySQLdb
from http.server import BaseHTTPRequestHandler, HTTPServer
 
app_server_ipv4 = "192.168.122.144" 
app_server_port = "8080"
app_db_ipv4 = "127.0.0.1"
authorized_ipv4 = []

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # POST
    #def do_POST(self):


    # GET
    def do_GET(self):
        # Send response status code
        authorized = False
        for ip in authorized_ipv4:
            if (i == self.client_address[0]):
                authorized = True
        print("It's headers of http request: " +  str(self.headers.keys()))

        for header in self.headers.keys():
            if (header == "Authorization"):
                print("Value of Authorization header login: " + self.headers.get("Authorization").split(' ')[0])      
                print("Value of Authorization header password: " + self.headers.get("Authorization").split(' ')[1])      




        if (authorized == False):
            self.send_response(401)
            self.send_header('WWW-Authenticate','Login Password"')
            self.end_headers()
            return
        else:

            self.send_response(200)
 
        # Send headers
            self.send_header('Content-type','text/html')
            self.end_headers()

            print("Client address " + str(self.client_address))
        # Send message back to client
            message = "Hello world!"
        # Write content as utf-8 data
            self.wfile.write(bytes(message, "utf8"))
            return
 
def run():
    print('starting server...')
 
    # Server settings
    # Choose port and specify app_server's ip address
    server_address = (app_server_ipv4, int(app_server_port))

    # Create instance of HTTPServer with http server settings (first argument and my RequestHandler 
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

    print('running server...')
    httpd.serve_forever()
 
 
run()


