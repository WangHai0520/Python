#生成list进行求和
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

#while循环
# sum = 0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print(sum)

#break 退出循环
# n=1
# while n <= 100:
#     if n >= 10:
#         break
#     print(n)
#     n=n+1
# print('END')

#continue 跳过单次循环
n = 0
while n < 10:
    n=n+1
    if n%2 == 0:    #note:注意是双等号
        continue
    print(n)

