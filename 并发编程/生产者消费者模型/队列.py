from multiprocessing import Queue

# 队列：先进先出
q = Queue(3)

# .put()可以放入任何对象
q.put('a1')
q.put({'a':1})
q.put(1)

print(q.get())
print(q.get())
print(q.get())

# 超过队列设置的值不会报错
# print(q.get())
