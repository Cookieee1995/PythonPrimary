import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('127.0.0.1',8080))
while True:
    msgs = input('输入信息：')
    if msgs == 'q':
        client.send(msgs.encode('utf-8'))
        break
    client.send(msgs.encode('utf-8'))

    recv_msgs = client.recv(1024)
    print(recv_msgs.decode('utf-8'))

client.close()