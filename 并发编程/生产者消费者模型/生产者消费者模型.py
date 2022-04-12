from multiprocessing import Process,Queue
import time,random
# 生产者
def producer(name,q):
    # 生产者生产，产生的结果放进队列中
    for i in range(10):
        s = '饺子{}'.format(i)
        time.sleep(random.randint(1,3))
        q.put(s)
        print('{}厨师生产了{}'.format(name,s))

# 消费者
def customer(name,q):
    # 消费者从队列取出信息
    while True:
        res = q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('{}吃了{}'.format(name,res))

if __name__ == '__main__':

    q = Queue()
    p = Process(target=producer,args=('egon',q))
    c = Process(target=customer,args=('alex',q))

    p.start()
    p.join()
    q.put(None)
    c.start()
