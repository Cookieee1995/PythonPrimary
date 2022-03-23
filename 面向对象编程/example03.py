from example02 import SecondClass
import math

class ThirdClass(SecondClass):

    def __init__(self,value):
        self.data = value

    def __add__(self,other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: {}]'.format(self.data)

    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.display()
print(a)

b = a + 'xyz'
b.display()
print(b)

a.mul(3)
print(a)