import json
import socket
import struct
download_dir = '/网络编程/实现下载功能/加上md5校验/tasks'

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'
client.connect(IP_PORT)

while True:
    cmd = input('>>> ').strip()
    if not cmd:continue
    client.send(cmd.encode(utf_8))

    obj = client.recv(4)
    header_size = struct.unpack('i',obj)[0]

    header_bytes = client.recv(header_size)
    header_json = header_bytes.decode(utf_8)
    header_dict = json.loads(header_json)

    filename = header_dict['filename']
    abs_path = r'{}{}'.format(download_dir,filename)
    size = header_dict['size']

    recv_size = 0
    with open(filename,'wb') as f:
        while recv_size < size:
            line = client.recv(1024)
            f.write(line)
            recv_size += len(line)
client.close()