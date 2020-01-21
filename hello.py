#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

print("Content-Type: text/html")

# Question 1
# print(os.environ)

# Question 2
# print(os.environ["QUERY_STRING"])

# Question 3
# print(os.environ["HTTP_USER_AGENT"])

# Question 4
print(login_page())

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")