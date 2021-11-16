"""
MyHTTPServer

A simple Python web server which implements GET and POST
"""

import socket
import socketserver
import http.server
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        page = "<html><body><h1>Hello World</h1><p>This is a python web server</p></body></html>"
        self.wfile.write(page.encode())

ADDRESS = '127.0.0.1'
PORT = 12345
httpd = socketserver.TCPServer((ADDRESS, PORT), Handler)
httpd.serve_forever()