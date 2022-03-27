import socket
import subprocess

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

IP_PORT = ('127.0.0.1',8080)
utf_8 = 'utf-8'

server.bind(IP_PORT)
server.listen(5)

while True:
    conn,addr = server.accept()

    while True:
        try:
            recv_msgs = conn.recv(1024).decode(utf_8)
            if not recv_msgs:
                break
            print(recv_msgs)

            obj = subprocess.Popen(recv_msgs,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()


            conn.send((stdout+stderr))
        except Exception:
            break
