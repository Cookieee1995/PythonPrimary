# 同一个进程内的多个线程是共享该线程的资源
# 创建新的线程开销远远小于开启新的进程

from threading import Thread

class MyThread(Thread):

    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        print('%s is running' % self.n)

if __name__ == '__main__':
    t = MyThread(2)
    t.start()
    print('主')