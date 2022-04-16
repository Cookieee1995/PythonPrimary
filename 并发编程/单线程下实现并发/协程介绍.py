# 协程：单线程下实现并发，用户从应用程序级别控制单线程下任务的切换，注意一定要遇到IO才切

# import gevent
#
# def eat(name):
#     print('%s eat 1' % name)
#     gevent.sleep(2)
#     print('%s eat 2'% name)
#
# def play(name):
#     print('%s play 1' % name)
#     gevent.sleep(1)
#     print('%s play 2'% name)
#
# g1 = gevent.spawn(eat,'alex')
# g2 = gevent.spawn(play,'egon')
#
# # g1.join()
# # g2.join()
# # 或
# gevent.joinall([g1,g2])

from gevent import monkey;monkey.patch_all()        # 识别所有IO
import gevent,os

def eat():
    print('%s eat 1' % os.getpid())
    gevent.sleep(2)
    print('%s eat 2'% os.getpid())

def play():
    print('%s play 1' % os.getpid())
    gevent.sleep(1)
    print('%s play 2'% os.getpid())

g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)

# g1.join()
# g2.join()
# 或
gevent.joinall([g1,g2])