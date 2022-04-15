# 指定n秒后执行某些操作

from threading import Timer

def hello():
    print('hello,world')

# 1秒后执行
t = Timer(1,hello)
t.start()
