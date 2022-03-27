import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_PORT = ('127.0.0.1',8080)
utf_8 = 'utf-8'

client.connect(IP_PORT)

while True:

    cmd_msgs = input('输入：').encode(utf_8)
    if not cmd_msgs: continue
    client.send(cmd_msgs)

    recv_msgs = client.recv(1024).decode(utf_8)
    print(recv_msgs)