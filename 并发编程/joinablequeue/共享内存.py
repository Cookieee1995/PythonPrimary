from multiprocessing import Manager,Process

def work(d):
    d['count'] -= 1

if __name__ == '__main__':
    m = Manager()
    d = m.dict({"count":100})
    p_l = []
    for i in range(100):
        p = Process(target=work,args=(d,))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    print(d)