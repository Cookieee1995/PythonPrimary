from multiprocessing import Process
import time

def foo():
    print(123)
    time.sleep(1)
    print('end123')

def bar():
    print(456)
    time.sleep(3)
    print('end456')

if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)

    p1.daemon = True
    p1.start()

    p2.start()

    print('main.....')


# 可能的输出：
# 123
# main.....
# 456
# end456
# 在主进程print('main.....')结束之前，p1进程先开始运行，等到主程序运行结束，p1作为守护进程在主进程结束后立即停止，无法打印end123。
# p2不是守护进程，正常运行结束。

# main.....
# 456
# end456
# 主程序执行完,p1进程也没有开始运行。