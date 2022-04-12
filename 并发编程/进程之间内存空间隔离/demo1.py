from multiprocessing import Process
n = 100
def work():
    global n
    n = 0
    print('子进程',n)

p = Process(target=work)
p.start()
print('主进程',n)