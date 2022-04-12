import hashlib
import socket,os,json,struct

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(IP_PORT)

while True:
    cmd = input('>>> ').strip()
    if cmd == 'quit':break
    if not cmd:continue
    client.send(cmd.encode(utf_8))

    obj = client.recv(4)
    header_length = struct.unpack('i',obj)[0]

    header_bytes = client.recv(header_length)
    header_json = header_bytes.decode(utf_8)
    header_dict = json.loads(header_json)

    filename = header_dict['filename']
    filesize = header_dict['filesize']

    recv_size = 0
    with open(filename,'wb') as f:
        m = hashlib.md5()
        while recv_size < filesize:
            data = client.recv(1024)
            f.write(data)
            m.update(data)
            recv_size += len(data)
        md5 = m.hexdigest()
        print(md5)
    recv_md5 = client.recv(1024)
    print(recv_md5.decode(utf_8))