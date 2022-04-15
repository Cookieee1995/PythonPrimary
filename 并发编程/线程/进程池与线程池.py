# 进程池
# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# import time,random,os

# def work(n):
#     print('%s is running' % os.getpid())
#     time.sleep(random.randint(1,3))
#     return n ** 2
# if __name__ == '__main__':

    # executor = ProcessPoolExecutor(4)
    # futures = []
    # for i in range(10):
    #     future = executor.submit(work,i)
    #     futures.append(future)

    # executor.shutdown(wait=True)
    # print('主')
    # for obj in futures:
    #     print(obj.result())

# 线程池
# import os,time,random
# import threading
# from concurrent.futures import ThreadPoolExecutor
#
# def work(n):
#     print('%s is running' % threading.current_thread().getName())
#     time.sleep(random.randint(1,3))
#     return n ** 2
#
# if __name__ == '__main__':
#     execute = ThreadPoolExecutor()
#     futures = []
#     for i in range(40):
#         future = execute.submit(work,i)
#         futures.append(future)
#     execute.shutdown(wait=True)
#     print('主')
#     for obj in futures:
#         print(obj.result())

# map方法(拿不到结果)
import os,time,random
# from concurrent.futures import ProcessPoolExecutor
#
# def work(n):
#     print('%s is working' % os.getpid())
#     time.sleep(random.randint(1,3))
#     return n ** 2
#
# if __name__ == '__main__':
#     execute = ProcessPoolExecutor()
#
#     execute.map(work,range(10))
#     execute.shutdown(wait=True)
#     print('主')


# 回调函数
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import requests,os,time,random
from multiprocessing import Pool,Process

def get(url):
    print('%s GET %s' %(os.getpid(),url))
    response = requests.get(url)
    time.sleep(random.randint(3,6))
    if response.status_code == 200:
        return {'url':url,'text':response.text}

def parse(future):
    dic = future.result()
    print('%s PARSE %s' %(os.getpid(),dic['url']))
    time.sleep(1)
    res = '%s:%s\n' %(dic['url'],len(dic['text']))
    with open('db.txt','a') as f:
        f.write(res)

if __name__ == '__main__':
    urls = [
        'https://www.baidu.com/',
        'https://www.python.org/',
        'https://www.openstack.org/',
        'https://www.help.github.com/',
        'https://www.sina.com.cn/',
    ]

    execute = ProcessPoolExecutor()
    start_time = time.time()
    objs = []
    for url in urls:
        execute.submit(get,url).add_done_callback(parse)


    print('主',(time.time()-start_time))

