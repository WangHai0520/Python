age = input()
age = int(age)
#必须先把str转换成整数
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')