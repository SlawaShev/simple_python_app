#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        print("We are in handler")
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
    print('starting server...')
 
    # Server settings
    # Choose port 8081 and specify app_server's ip address
    server_address = ('192.168.122.144', 8081)

    # Create instance of HTTPServer with http server settings (first argument and my RequestHandler 
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)

    print('running server...')
    httpd.serve_forever()
 
 
run()


