from http.server import HTTPServer, BaseHTTPRequestHandler

import requests

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with requests.get(self.path, stream=True) as res:
            self.send_response(res.status_code)
            for key, value in res.headers.items():
                self.send_header(key, value)
            self.end_headers()
        
            print(res.raw.read())
            self.wfile.write(res.raw.read())

address = ("127.0.0.1", 8080)
server = HTTPServer(address, MyRequestHandler)
server.serve_forever()