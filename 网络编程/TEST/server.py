import socket,subprocess,struct,json

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

# 创建server对象
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 建立连接并等待
server.bind(IP_PORT)
server.listen(5)

# 连接循环
while True:
    conn,addr = server.accept()

    # 通信循环
    while True:
        try:
            # 收命令
            recv_cmd = conn.recv(1024).decode(utf_8)
            if not recv_cmd:break

            obj = subprocess.Popen(recv_cmd,shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 制作报头
            head_dict = {
                'filename':'get_{}.txt'.format(recv_cmd),
                'length':len(stdout)+len(stderr),
                'md5':'12h912u28918921r89'
            }

            # 获得报头长度
            head_str = json.dumps(head_dict)
            head_bytes = head_str.encode(utf_8)
            head_len = len(head_bytes)
            head_length = struct.pack('i',head_len)

            # 发报头长度
            conn.send(head_length)
            # 发报头
            conn.send(head_bytes)
            # 发信息
            conn.send(stdout)
            conn.send(stderr)


        except Exception:
            break


