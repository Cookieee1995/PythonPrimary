from multiprocessing import Process
import time,random,os

def work():
    print(f'子进程的pid{os.getpid()}，父进程的pid{os.getppid()}')
    time.sleep(3)

if __name__ == '__main__':
    p1 = Process(target=work)
    p2 = Process(target=work)
    p3 = Process(target=work)
    p1.start()
    p2.start()
    p3.start()
    p1.join()    # 主进程等得，等待子进程结束后，主进程再执行后面的代码

    print('主进程',os.getpid(),os.getppid())
    time.sleep(100000)