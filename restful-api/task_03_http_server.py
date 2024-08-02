# simple_api_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_not_found()

    def handle_root(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')

    def handle_data(self):
        response = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_status(self):
        response = {
            "status": "OK"
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def handle_not_found(self):
        self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "error": "Endpoint not found"
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()

