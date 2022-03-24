import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

utf = 'utf-8'
IP_PORT = ('127.0.0.1',8080)
client.connect(IP_PORT)

while True:
    send_msgs = input('>>>: ')
    if not send_msgs: continue
    client.send(send_msgs.encode(utf))

    recv_msgs = client.recv(1024)
    recv_data = recv_msgs.decode(utf)
    print('成功接收{}'.format(recv_data))