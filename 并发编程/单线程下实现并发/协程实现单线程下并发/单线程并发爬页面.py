import requests,gevent
from threading import current_thread
from gevent import monkey;monkey.patch_all()
def get(url):
    print('%s get %s' % (current_thread().getName(),url))
    response = requests.get(url)
    if response.status_code == 200:
        # print('%s 下载 %s:%s' %(current_thread().getName(),url,len(response.text)))
        # return {'url':len(response.text)}
        print({'url':len(response.text)})

g1 = gevent.spawn(get,'https://www.baidu.com/')
g2 = gevent.spawn(get,'https://www.python.org/')
g3 = gevent.spawn(get,'https://www.bing.com/')

# gevent.joinall([g1,g2,g3])
g1.join()
g2.join()
g3.join()

print(g1.value)
print(g2.value)
print(g3.value)