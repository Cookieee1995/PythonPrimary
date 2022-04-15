from threading import Thread
import os

n = 100
def work():
    global n
    n = 0

if __name__ == '__main__':
    t = Thread(target=work)
    t.start()
    t.join()
    print(t.is_alive())
    print('主线程',n)