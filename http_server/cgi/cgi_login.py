#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
username = form.getfirst("username", "не задано")
password = form.getfirst("password", "не задано")

print("DEBUG \n username is {0} and password is {1}".format(username, password))

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(username))
print("<p>TEXT_2: {}</p>".format(password))

print("""</body>
        </html>""")

