import socket

IP_PORT = ('127.0.0.1',8080)
UTF_8 = 'UTF-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(IP_PORT)

while True:
    send_msg = input('>>> ').strip()
    if not send_msg:continue
    client.send(send_msg.encode(UTF_8))
    data = client.recv(1024)
    print(data.decode(UTF_8))