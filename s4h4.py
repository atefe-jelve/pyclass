#ATEFE-JELVE__THURSDAY14-18
#DEFINE-square-union
def union1(a,b):
    result = (a**2)+(2*a*b)+(b**2)
    return result

def union2(a,b):
    result = (a**2)-(2*a*b)-(b**2)
    return result

def union3(a,b):
    result = (a**3)+(3*(a**2)*b)+(3*a*(b**2))+(b**2)
    return result

def union4(a,b):
    result = (a**3)-(3*(a**2)*b)+(3*a*(b**2))-(b**2)
    return result

a = int(input('enter the first number:\n'))
b = int(input('enter the secend number:\n'))
power = (input('enter  number "'"1"'" for calculate (a+b)^2 or "'"2"'" for (a-b)^2  \n or "'"3"'" for (a+b)^3 or "'"4"'" for (a-b)^3  : \n'))

if power == '1':
   result = union1(a,b)
elif power == '2':
    result = union2(a,b)
elif power == '3':
    result = union3(a,b)
elif power == '4':
    result = union4(a,b)

print(result)
