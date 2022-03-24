import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_PORT = ('127.0.0.1',8080)
utf = 'utf-8'

client.connect(IP_PORT)
while True:
    send_msgs = input('输入：').encode(utf)
    if not send_msgs:
        continue
    client.send(send_msgs)

    recv_msgs = client.recv(1024).decode(utf)
    print(recv_msgs)

client.close()