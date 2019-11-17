#!/usr/bin/python3

#import MySQLdb
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

app_server_ipv4 = "192.168.122.144" 
app_server_port = "8080"
app_db_ipv4 = "127.0.0.1"
authorized_ipv4 = []

# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # POST
    #def do_POST(self):


    # GET
    
    def do_GET(self):
        try:
            # Figure out what exactly is being requested.
            full_path = os.getcwd() + self.path

            # It doesn't exist...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))

            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)

            # ...it's something we don't handle.
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))

        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)
        
        # Function for handling of file. It sends file as response.
    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
                self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """
        
        # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

        # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


#        # Send response status code
#        authorized = False
#        for ip in authorized_ipv4:
#            if (i == self.client_address[0]):
#                authorized = True
#        print("It's headers of http request: " +  str(self.headers.keys()))
#
#        for header in self.headers.keys():
#            if (header == "Authorization"):
#                print("Value of Authorization header login: " + self.headers.get("Authorization").split(' ')[0])      
#                print("Value of Authorization header password: " + self.headers.get("Authorization").split(' ')[1])      
#
#
#
#
#        if (authorized == False):
#            self.send_response(401)
#            self.send_header('WWW-Authenticate','Login Password"')
#            self.end_headers()
#            return
#        else:
#
#            self.send_response(200)
# 
#        # Send headers
#            self.send_header('Content-type','text/html')
#            self.end_headers()
#
#            print("Client address " + str(self.client_address))
#        # Send message back to client
#            message = "Hello world!"
#        # Write content as utf-8 data
#            self.wfile.write(bytes(message, "utf8"))
#            return
 
def run():
    print('starting server...')
 
    # Server settings
    # Choose port and specify app_server's ip address
    server_address = (app_server_ipv4, int(app_server_port))

    # Create instance of HTTPServer with http server settings (first argument and my RequestHandler 
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)

    print('running server...')
    httpd.serve_forever()
 
 
run()


