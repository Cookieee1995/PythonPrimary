from multiprocessing import Process
import time

def work(n):
    print('---->start')
    time.sleep(2)
    print('---->end')

if __name__ == '__main__':
    p1 = Process(target=work,args=(2,))
    p2 = Process(target=work,args=(2,))
    # p1.daemon = True      # 设置p1为守护进程
    p1.start()
    p2.daemon = True
    p2.start()
    print('主程序')        # 这行打印完意味着主程序结束，守护进程立刻结束

# 守护进程里不能再开进程