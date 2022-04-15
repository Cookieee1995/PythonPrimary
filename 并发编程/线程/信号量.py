from threading import Semaphore,Thread,current_thread
import time,random

def task():
    with sm:
        print('%s toliet' % current_thread().getName())
        time.sleep(random.randint(1,3))

if __name__ == '__main__':
    sm = Semaphore(5)
    for i in range(10):
        t = Thread(target=task)
        t.start()
