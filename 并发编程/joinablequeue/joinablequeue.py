# from multiprocessing import Process,Queue
# import time,random
#
# def producer(q,name,food):
#     for i in range(1,7):
#         res = '{}{}'.format(food,i)
#         q.put(res)
#         print(f'{name}生产了{res}')
#         time.sleep(random.randint(1,3))
#
# def customer(q,name):
#     while True:
#         res = q.get()
#         if res is None:break
#         print(f'{name}吃了{res}')
#         time.sleep(random.randint(1,3))
#
# if __name__ == '__main__':
#     # 创建进程池
#     q = Queue()
#
#     # 两个生产者进程
#     p1 = Process(target=producer,args=(q,'1','饺子'))
#     p2 = Process(target=producer,args=(q,'2','馄饨'))
#     # 两个消费者进程
#     c1 = Process(target=customer,args=(q,'a'))
#     c2 = Process(target=customer,args=(q,'b'))
#
#     p1.start()
#     p2.start()
#
#     c1.start()
#     c2.start()
#
#     # 等待所有生产者进程结束
#     p1.join()
#     p2.join()
#     # 有几个消费者就发几个空的信号
#     q.put(None)
#     q.put(None)
# 无序


from multiprocessing import Process,Queue,JoinableQueue
import time,random

def producer(q,name,food):
    for i in range(1,7):
        res = '{}{}'.format(food,i)
        q.put(res)
        print(f'{name}生产了{res}')
        time.sleep(random.randint(1,3))

def customer(q,name):
    while True:
        res = q.get()
        if res is None:break
        print(f'{name}吃了{res}')
        time.sleep(random.randint(1,3))
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()

    p1 = Process(target=producer,args=(q,'1','饺子'))
    p2 = Process(target=producer,args=(q,'2','馄饨'))

    c1 = Process(target=customer,args=(q,'a'))
    c2 = Process(target=customer,args=(q,'b'))

    p1.start()
    p2.start()

    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()

    p1.join()
    p2.join()
# 有序