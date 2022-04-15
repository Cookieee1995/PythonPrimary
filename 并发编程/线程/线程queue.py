import queue

# q = queue.Queue(3)       # 队列
# q.put(3)
# q.put(2)
# q.put(4)
# q.put(5)

# print(q.get())
# print(q.get())
# print(q.get())

# 优先级队列
q = queue.PriorityQueue(3)
# 数字越小，优先级越高
q.put((10,'aaa'))
q.put((7,'aca'))
q.put((2,'aba'))
# q.put((30,'daa'))
# 优先级相同，按后面内容的ASCII码
print(q.get())
print(q.get())
print(q.get())
# -----------------------
queue.LifoQueue()       # 后进先出，堆栈