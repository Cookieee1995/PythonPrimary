# 生成器表达式返回生成器对象
# 生成器是一个以简单的方式来完成迭代并且返回可以迭代对象的函数，是一种一边循环一边计算的机制。

# print('-'*19,'创建生成器','-'*19)
# gen1 = (x for x in range(5))
# print(type(gen1))
# 调用生成器需要使用next()方法，每调用一次获取一次生成器的下一个返回值，知道计算到最后一个元素。
# 如果生成器中的元素被调用完，再一次调用则会抛出StopIteration
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen1))
# print(next(gen))
# print('-'*40)
# 生成器是可迭代对象，也可以使用for循环获取返回值
# gen2 = (x for x in range(5))
# for i in gen2:
#     print(i)
# print('-'*40)
# 通过在函数中使用yield创建生成器
# def gen3(num):
#     for i in range(num):
#         yield i

# g = gen3(5)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# 调用函数后在yield处会保存当前函数的执行状态，当函数返回值后，又回到之前保存的状态继续执行。
# 当调用包含yield语句的函数时不会立即执行，只是返回一个生成器，当程序通过next()函数调用或遍历生成器时，函数才会真正执行，
# 每使用一次next()函数返回一个值，然后冻结执行，直到下次使用next()函数才会继续执行。

print('-'*19,'send方法','-'*19)
# send方法用于传递参数，实现与生成器的交互。send()可以接收一个参数，并将参数传递给接收yield语句返回值的变量，这就使得程序要有一个变量来接收yield语句的值。
def gen_send(num):
    for i in range(num):
        temp = yield i
        print(temp)

g = gen_send(5)
print(next(g))
print(next(g))
print(g.send("send发送参数"))
print(g.send(None))     # next()相当于send(None)
print(g.send(None))

# 当程序运行到yield时会被暂时挂起，等待生成器调用send方法，
# 当使用send()再次调用时，send()中的参数会被传递给用来临时接收的变量temp，然后继续下一步操作，直到没有参数可传递时发送None。