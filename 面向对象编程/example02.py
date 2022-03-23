from example01 import FirstClass
class SecondClass(FirstClass):

    def display(self):
        print('Current value = "{}"'.format(self.data))

z = SecondClass()
z.setdata(42)
z.display()