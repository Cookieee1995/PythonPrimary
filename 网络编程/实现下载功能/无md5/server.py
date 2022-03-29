import socket,os,struct,json

# 默认值
IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

# 建立socket对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 建立连接
server.bind(IP_PORT)
server.listen(5)

def get(conn,path_name):

    # 制作报头
    header_dict = {
        'file_name':os.path.basename(path_name),
        'file_size':os.path.getsize(path_name),
        'md5':'a7fysf'
    }
    print(header_dict)

    # 报头长度
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode(utf_8)
    conn.send(struct.pack('i',len(header_bytes)))

    # 发报头
    conn.send(header_bytes)
    # 发文件内容
    with open(path_name,'rb') as f:
        for line in f:
            conn.send(line)

# 连接循环
while True:
    conn,addr = server.accept()
    # 通信循环
    while True:
        try:
            # 收到命令
            recv_cmd = conn.recv(1024)
            if not recv_cmd:break
            # 把收到的字节形式的命令转成字符串，再分割成列表
            cmd,path_name = recv_cmd.decode(utf_8).split()
            print(cmd,'|',path_name)
            # 判断cmd是什么命令
            if cmd == 'get':
                get(conn,path_name)

        except Exception:
            break
