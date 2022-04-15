# 子线程与主线程pid相同

from threading import Thread
import os

# def work():
#     print('%s is running' % os.getpid())

# if __name__ == '__main__':
#     t = Thread(target=work)
#     t.start()
#     print('主线程',os.getpid())

# 同一进程内的多个线程共享该进程的资源

n = 100
def work():
    global n
    n = 0

if __name__ == '__main__':
    t = Thread(target=work)
    t.start()
    t.join()
    print('主线程',n)