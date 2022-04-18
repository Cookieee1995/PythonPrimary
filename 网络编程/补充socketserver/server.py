import socketserver

class MyTCPhandler(socketserver.BaseRequestHandler):

    def handle(self):
        # 通信循环：
        print(self.request)     # == conn,addr
        while True:
            try:
                data = self.request.recv(1024)
                if not data:break
                self.request.send(data.upper())
            except Exception:
                break



if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyTCPhandler)
    server.serve_forever()