import socket
from multiprocessing import Process

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

client.connect(IP_PORT)

while True:
    msg = input('>>> ').strip()
    if not msg:continue
    client.send(msg.encode(utf_8))
    data = client.recv(1024)
    print(data.decode(utf_8))