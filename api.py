from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hermes Backend API Online')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), SimpleAPI)
    print('Hermes Backend running on port 5000...')
    server.serve_forever()
