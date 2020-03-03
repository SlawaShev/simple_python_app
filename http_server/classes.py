import os

class case_cgi_request(object):
    '''Handle cgi request'''
    def script_path(self, handler):
        return os.path.join(handler.full_path, \
        (handler.path.split("?"))[0])

    def test(self, handler):
        return os.path.isfile(handler.full_path.split("?")[0])

    def shell_command(self, handler):
        command = ""
        for char in str(handler.path.split("?")[1]):
            if (char == '&'):
                command += "'&'"
            else:
                command += char
        return command
#        print(str(command))


    def act(self, handler):
        print("Everything alright")
        self.shell_command(handler)
        os.system("python3 " + str(handler.full_path.split("?")[0]) + " " +  self.shell_command(handler))
        #print("python3 " + str(handler.full_path.split("?")[0]) + " " +  str(self.shell_command(handler)))
        #print(handler.full_path)
        handler.handle_file(handler.full_path.split("?")[0])

class case_directory_index_file(object):
    '''Serve index.html page for a directory.'''

    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')

    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))

    def act(self, handler):
        handler.handle_file(self.index_path(handler))


class ServerException(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # It's for your custom code

class case_no_file(object):
    '''File or directory does not exist.'''

    def test(self, handler):
        return not os.path.exists(handler.full_path)

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.full_path))


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


