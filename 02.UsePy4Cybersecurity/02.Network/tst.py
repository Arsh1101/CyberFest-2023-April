import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.recv(1024)
        self.request.sendall(b"Hello, world!")

if __name__ == "__main__":
    HOST, PORT = "localhost", 5
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print(f"Listening on port {PORT}...")
        server.serve_forever()
