from multiprocessing import Process
import socket,os,struct,json,hashlib

IP_PORT = ('127.0.0.1',8888)
utf_8 = 'utf-8'

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

server.bind(IP_PORT)
server.listen(5)

def get(conn,filename):

    header_dict = {
        'filename':os.path.basename(filename),
        'filesize':os.path.getsize(filename),
    }

    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode(utf_8)

    conn.send(struct.pack('i',len(header_bytes)))
    conn.send(header_bytes)

    with open(filename,'rb') as f:
        m = hashlib.md5()
        for line in f:
            conn.send(line)
            m.update(line)
        md5 = m.hexdigest()
        conn.send(md5.encode(utf_8))
        print(md5)

def run(conn):
    while True:
        try:
            recv_cmd = conn.recv(1024).decode(utf_8)
            if not recv_cmd:break
            cmd,filename = recv_cmd.split()
            if cmd == 'get':
                get(conn,filename)
        except Exception:
            break

if __name__ == '__main__':
    while True:
        conn,addr = server.accept()
        p = Process(target=run,args=(conn,))
        p.start()
