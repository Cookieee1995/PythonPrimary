# def和lambda都能完成同样种类的功能

def func1(x,y,z):
    return x+y+z
print(func1(2,3,4))

# f = lambda x,y,z: x+y+z
# print(f(2,3,4))

# map将被传入的函数作用到一个可迭代对象的每一个元素上，并且返回包含了所有这些函数调用结果的一个列表：
counters = [1,2,3,4]
l1 = list(map((lambda x:x+3),counters))
print(l1)

# 选择可迭代对象中的元素
print(list(filter((lambda x: x > 0),range(-5,5))))

#
from functools import reduce
print(reduce((lambda x,y:x+y),[1,2,3,4]))
print(reduce((lambda x,y:x*y),[1,2,3,4,5]))