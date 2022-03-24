import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
utf = 'utf-8'
IP_PORT = ('127.0.0.1',8888)
server.bind(IP_PORT)

server.listen(5)

while True:
    conn,addr = server.accept()
    while True:
        try:
            recv_msgs = conn.recv(1024)
            if not recv_msgs:
                break
        except Exception:
            break
        recv_data = recv_msgs.decode(utf)
        print(recv_data)
        send_msgs = recv_data.upper().encode(utf)
        conn.send(send_msgs)

conn.close()
server.close()