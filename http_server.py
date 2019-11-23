#!/usr/bin/python3

#import MySQLdb
from http.server import BaseHTTPRequestHandler, HTTPServer
import os

app_server_ipv4 = "192.168.122.144" 
app_server_port = "80"
app_db_ipv4 = "127.0.0.1"

class case_no_file(object):
    '''File or directory does not exist.'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(self.path))


class case_existing_file(object):
    '''File exists'''

    def test(self, handler):
        return os.path.isfile(handler.full_path)

    def act(self, handler):
        handler.handle_file(handler.full_path)

            
class case_always_fail(object):
    '''Base case if nothing else worked.'''

    def test(self, handler):
        return True

    def act(self, handler):
        raise ServerExceptions("Unknown object '{0}'".format(handler.path))


# HTTPRequestHandler class
class HTTPServer_RequestHandler(BaseHTTPRequestHandler):
    
    Cases = [case_no_file(), case_existing_file(), case_always_fail()]

    # POST
    #def do_POST(self):


    # GET
    def do_GET(self):
        try:
            # Figure out what exactly is being requested.
            self.full_path = os.getcwd() + self.path

            # Figure out how to handle it.
            for case in self.Cases:
                handler = case
                if handler.test(self):
                    handler.act(self)
                    break
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


