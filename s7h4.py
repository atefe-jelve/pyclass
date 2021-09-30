#ATEFE-JELVE__THURSDAY14-18
#FIBONACHI-WHIT-2-MODE

# fibo=[1,1]
# f1,f2=1,1
# n = int(input('enter your number for fibo calc:\n'))
# if n==1:
#     print(1)
# elif n==2:
#     print(1,1)
# elif n>2:
#     for i in range(3,n+1):
#         f3 = f1+f2
#         fibo.append(f3)
#         f1,f2=f2,f3
#     print(fibo)
# else:
#     print('invalid input')


def fibo(n):
    if n<0:
        print('incorect input')
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
n = int(input('enter your number for fibo calc:\n'))
# print(fibo(0))
# print(fibo(1))
print((f' number of fibo is:  ""  {fibo(n)}  ""'))
# print([fibo(n) for n in range(0,10)])
