# This file is an example web server,
# we do not recommend using it for
# production use.

# Code is copied from https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler
# and has been modified by me to automatically use the script directory instead of your working directory

import http.server
import socketserver
import os

os.chdir(os.path.dirname(__file__))

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()