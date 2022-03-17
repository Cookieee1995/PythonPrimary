# 迭代器用于迭代操作的对象，它像列表一样可以迭代获取其中的每一个元素，任何实现__next__方法的对象都可以成为迭代器。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前进不会后退。生成器也是一种迭代器。

# Python中通常使用for循环对某个对象进行遍历，此时被遍历的这个对象就是可迭代对象。
# 只要是实现了__iter__()或__getitem__()方法的对象，就可以成为可迭代对象。

print('-'*20,'创建迭代器','-'*20)
list = [1,2,3,4,5]
it = iter(list)
print(type(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))