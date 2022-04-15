import requests,os,time,random
from multiprocessing import Pool,Process

def get(url):
    print('%s GET %s' %(os.getpid(),url))
    response = requests.get(url)
    time.sleep(random.randint(3,6))
    if response.status_code == 200:
        return {'url':url,'text':response.text}

def parse(dic):
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

    p = Pool(2)
    start_time = time.time()
    objs = []
    for url in urls:
        obj = p.apply_async(get,args=(url,),callback=parse)
        objs.append(obj)
    p.close()
    p.join()

    print('主',(time.time()-start_time))

