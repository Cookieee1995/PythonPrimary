from multiprocessing import Process
import os,time,random

def task():
    print('{} is running'.format(os.getpid))
    time.sleep(random.randint(1,3))
    print('{} is end'.format(os.getpid()))


if __name__ == '__main__':
    p1 = Process(target=task)
    p2 = Process(target=task)
    p3 = Process(target=task)
    p1.start()
    p2.start()
    p3.start()
    print('main ')

# 有序