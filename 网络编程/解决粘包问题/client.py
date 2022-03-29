import socket,json,struct

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

client.connect(IP_PORT)

while True:

    send_cmd = input('>>> ').strip()
    if not send_cmd:continue
    if send_cmd == 'quit':break
    client.send(send_cmd.encode(utf_8))

    recv_len = struct.unpack('i',client.recv(4))[0]
    head_bytes = client.recv(recv_len)
    head_json = head_bytes.decode(utf_8)
    head = json.loads(head_json)

    size = head['size']
    filename = head['filename']

    recv_size = 0
    recv_data = b''
    with open(filename,'wb') as f:
        while recv_size < size:
            data = client.recv(1024)
            f.write(data)
            recv_data += data
            recv_size += len(data)
    print(recv_data.decode(utf_8))