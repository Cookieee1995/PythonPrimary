from multiprocessing import Process,Queue
import time,random

def producer(q):
    for i in range(10):
        res = '饺子{}'.format(i)
        q.put(res)
        print('厨师包了{}'.format(res))
        time.sleep(random.randint(1,3))

def customer(q):
    while True:
        res = q.get()
        if res is None:break
        print('我吃了{}'.format(res))
        time.sleep(random.randint(1,3))


if __name__ == '__main__':
    q = Queue()

    p = Process(target=producer,args=(q,))
    c = Process(target=customer,args=(q,))

    p.start()
    p.join()
    q.put(None)
    c.start()