from multiprocessing import Process
import time

def work(name,n):
    print(f'{name} is working...')
    time.sleep(n)
    print(f'{name} works finish.')

if __name__ == '__main__':
    p1 = Process(target=work,args=('alex',1))
    p1.start()
    p1.terminate()
    # time.sleep(1)
    print(p1.is_alive())
    print('主进程')