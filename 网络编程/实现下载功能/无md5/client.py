import socket,struct,json

# 默认值
import struct

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

# 建立socket对象
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务端
client.connect(IP_PORT)

# 通信循环
while True:
    cmd = input('>>> ').strip()     # example:get /home/cookieee/下载/bleach.png
    if not cmd:continue
    if cmd == 'quit':break
    client.send(cmd.encode(utf_8))

    # 收报头长度
    obj = client.recv(4)
    header_len = struct.unpack('i',obj)[0]

    # 收报头
    header_bytes = client.recv(header_len)
    header_json = header_bytes.decode(utf_8)
    header_dict = json.loads(header_json)

    # 文件名、文件大小
    file_name = header_dict['file_name']
    file_size = header_dict['file_size']

    # 收文件
    recv_size = 0
    with open(file_name,'wb') as f:
        while recv_size < file_size:
            data = client.recv(1024)
            f.write(data)
            recv_size += len(data)
