# 方式一
from multiprocessing import Process
import time

def work(name):

    print('{} is working...'.format(name))
    time.sleep(3)
    print(f'{name} works finish')

# windows 下开启进程
if __name__ == '__main__':
    p1 = Process(target=work,args=('wu1',))
    p1.start()
    p2 = Process(target=work,kwargs={'name':'wu2'})
    p2.start()
    print('主进程')

# linux 下开启进程，无main方法
p3 = Process(target=work,args=('wu3',))
p3.start()