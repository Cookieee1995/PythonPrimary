# 方式二

from multiprocessing import Process
import time

class Work(Process):

    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):

        print('{} is working'.format(self.name))
        time.sleep(3)
        print(f'{self.name} works finish')

if __name__ == '__main__':
    p1 = Work('wu1')
    p2 = Work('wu2')
    p3 = Work('wu3')
    p1.start()
    p2.start()
    p3.start()
    print('主进程')
