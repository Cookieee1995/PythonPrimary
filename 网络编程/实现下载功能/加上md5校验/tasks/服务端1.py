import os.path
import socket,json,struct

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(IP_PORT)
server.listen(5)

def get(conn,filename):

    #
    header_dict = {
        'filename':os.path.basename(filename),
        'filename_whole':filename,
        'size':os.path.getsize(filename),
        'md5':'12f11f1'
    }
    print(header_dict)
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode(utf_8)

    conn.send(struct.pack('i',len(header_bytes)))
    conn.send(header_bytes)

    with open(filename,'rb') as f:
        for line in f:
            conn.send(line)

while True:
    conn,addr = server.accept()
    while True:
        try:
            data = conn.recv(1024)
            cmd,filename = data.decode(utf_8).split()

            if cmd == 'get':
                get(conn,filename)



            if not data:break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
server.close()