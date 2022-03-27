import socket,subprocess,struct,json

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

# 建立客户端
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务端
client.connect(IP_PORT)

# 通信循环
while True:
    # 发
    cmd_message = input('>>> ').strip()
    if cmd_message == 'quit':break
    if not cmd_message:break
    client.send(cmd_message.encode(utf_8))

    # 收
    # 先收报头长度
    head_length = client.recv(4)
    head_len = struct.unpack('i',head_length)[0]

    # 根据报头长度收报头
    head_bytes = client.recv(head_len)
    head_dict = json.loads(head_bytes.decode(utf_8))

    # 从报头中提取信息
    file_length = head_dict['length']
    filename = head_dict['filename']

    # 收
    recv_cmd = b''
    recv_length = 0
    with open(filename,'ab') as f:
        while recv_length < file_length:
            recv_data = client.recv(1024)
            recv_cmd += recv_data
            recv_length += len(recv_data)
        f.write(recv_cmd)
        print(recv_cmd.decode(utf_8))
