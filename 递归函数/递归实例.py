# 递归求和
def f1(n):
    if n == 0:
        return 0
    else:
        sum_num = n + f1(n-1)
        return sum_num

print(f1(10))

# 求阶乘
def f2(n):
    if n == 1:
        return 1
    else:
        return n * f2(n-1)

print(f2(5))

