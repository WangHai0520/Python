#函数
    #基础版
def my_abs(x):  #注意冒号不可少
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-23))
    #有参数检查
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x