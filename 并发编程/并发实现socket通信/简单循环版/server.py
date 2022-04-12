import socket
from multiprocessing import Process

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

server.bind(IP_PORT)
server.listen(5)

def run(conn):
    while True:
        try:
            recv_data = conn.recv(1024)
            if not recv_data:break
            conn.send(recv_data.upper())
        except Exception:
            break

if __name__ == '__main__':
    while True:
        conn,addr = server.accept()
        p = Process(target=run,args=(conn,))
        p.start()