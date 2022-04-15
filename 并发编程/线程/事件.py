import time
from threading import Event,current_thread,Thread

e = Event()

def check():
    print('%s 正在检测' % current_thread().getName())
    time.sleep(3)
    e.set()

def conn():
    print('%s 正在等待链接' % current_thread().getName())
    e.wait()
    print('%s 正在连接' % current_thread().getName())

if __name__ == '__main__':
    t1 = Thread(target=check)
    t2 = Thread(target=conn)
    t3 = Thread(target=conn)
    t4 = Thread(target=conn)

    t1.start()
    t2.start()
    t3.start()
    t4.start()