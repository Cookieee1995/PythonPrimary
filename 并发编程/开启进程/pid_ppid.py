import os
from multiprocessing import Process
import time

def work():

    print('子进程的pid{}，父进程的pid{}'.format(os.getpid(),os.getppid()))
    time.sleep(10)

if __name__ == '__main__':
    p1 = Process(target=work)
    p1.start()
    p2 = Process(target=work)
    p2.start()
    print('主进程{},主进程的父进程{}'.format(os.getpid(),os.getppid()))


p3 = Process(target=work)
p3.start()

# 子进程的pid5147，父进程的pid5137
# 主进程5137,主进程的父进程2177
# 子进程的pid5148，父进程的pid5137
# 子进程的pid5149，父进程的pid5137