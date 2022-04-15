from multiprocessing import Pool
import os,time,random

def work(n):
    print('{} is working'.format(os.getpid()))
    time.sleep(random.randint(1,3))
    return n ** 2

if __name__ == '__main__':
    p = Pool()
    objs = []
    for i in range(1,9):
        # 同步调用
        # res = p.apply(work,args=(i,))
        # print(res)

        # 异步调用
        obj = p.apply_async(work,args=(i,))
        objs.append(obj)
        print(obj.get())
    p.close()
    p.join()
    for obj in objs:
        print(obj.get())
    print('end----')

# 同步调用：提交完任务后，在原地等待任务结束，结束后立刻拿到结果
# 阻塞：正在运行的进程遇到IO进入阻塞状态
# 异步调用：提交完任务后不会在原地等待结果，会继续提交下一次任务，等到所有任务都结束，才get结果
# 非阻塞：可能是运行状态，也可能是就绪状态