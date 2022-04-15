# 主线程从执行角度就代表了该进程，主线程会在所有非守护线程都运行完毕才结束，守护线程就在主线程结束后结束

import time
from threading import Thread,current_thread

# def work():
#     print('%s is running' % current_thread().getName())
#     time.sleep(2)
#     print('%s is done' % current_thread().getName())

# if __name__ == '__main__':
#     t1 = Thread(target=work)
#     t1.daemon = True
#     t1.start()

    # t2 = Thread(target=work)
    # t2.start()
    # print('主')

def foo():
    print(123)
    time.sleep(4)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon = True
    t1.start()
    t2.start()

    print('main...')