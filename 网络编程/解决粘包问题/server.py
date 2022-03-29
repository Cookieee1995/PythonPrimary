import socket,json,struct,subprocess

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

server.bind(IP_PORT)
server.listen(5)

while True:
    conn,addr = server.accept()

    while True:
        try:
            recv_cmd = conn.recv(1024).decode(utf_8)
            if not recv_cmd:break

            obj = subprocess.Popen(recv_cmd,shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            head = {}
            head['filename'] = 'result of {}.txt'.format(recv_cmd)
            head['size'] = len(stdout)+len(stderr)
            head['md5'] = 'fas58679'

            head_json = json.dumps(head)
            head_bytes = head_json.encode(utf_8)

            conn.send(struct.pack('i',len(head_bytes)))
            conn.send(head_bytes)
            conn.send(stdout)
            conn.send(stderr)

        except Exception:
            break