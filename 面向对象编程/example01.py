class FirstClass:

    def setdata(self,value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

# x.setdata("king Arthur")
# x.display()

y.setdata(3.14159)
y.display()

x.data = "New Value"
x.anothername = 'spam'
x.display()