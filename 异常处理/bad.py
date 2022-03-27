# def gobad(x,y):
#     return x/y
#
# def gosouth(x):
#     print(gobad(x,0))
#
# gosouth(1)



def kaboom(x,y):
    print(x+y)

try:
    kaboom('[0,1,2]','spam')
    print('resuming here')
except TypeError:
    print('Hello world')
print('resuming here')

