from http.server import HTTPServer, BaseHTTPRequestHandler
import os, sys


class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = self.path[1:]
        if request == 'HelloWorld.html':
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            with open(os.path.join(sys.path[0], 'HelloWorld.html'), 'r') as f:
                self.wfile.write(f.read().encode())
        else:
            self.send_response(404)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('404 file not found'.encode())


def main():
    PORT = 8000
    HOST = '153.33.133.200'
    server = HTTPServer((HOST, PORT), helloHandler)
    print('Server Running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
