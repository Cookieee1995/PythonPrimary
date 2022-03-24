import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',8080))

server.listen(5)
while True:
    conn,addr = server.accept()


    while True:
        try:
            accept_msgs = conn.recv(1024)
            if not accept_msgs:
                break
        except Exception:
            break

        print(accept_msgs.decode('utf-8'))

        recv_msgs = '你好'
        conn.send(recv_msgs.encode('utf-8'))

    conn.close()
server.close()