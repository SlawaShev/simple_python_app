#!/usr/local/bin/python3

class cookie(object):
    '''This class is used for cookie handling'''
    def handle_cookie(self, handler):
        if "Cookie" not in handler.headers:
            self.set_cookie = True
        else:
            self.set_cookie = False


