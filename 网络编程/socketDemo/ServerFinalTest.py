import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
IP_PORT = ('127.0.0.1',8080)
utf = 'utf-8'

server.bind(IP_PORT)

server.listen(5)

while True:
    conn,addr = server.accept()

    while True:
        try:
            recv_msgs = conn.recv(1024).decode(utf)
            if not recv_msgs:
                break
            print('成功接收{}'.format(recv_msgs))

            send_msgs = conn.send(recv_msgs.encode(utf))
        except Exception:
            break


    conn.close()
server.close()