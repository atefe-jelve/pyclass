#ATEFE-JELVE__THURSDAY14-18
#AVG-NUMBERS-ENTER-BY-USER
# number = list()
# tool = 0
# sum_ = 0
# while tool < 10 :
#     entro = int(input('enter number:'))
#     number.append(entro)
#     sum_ = sum_ + entro
#     tool = len(number)
# avg =  sum_ / tool
# print(avg)

number = list()
tool = 0
sum_ = 0
for i in range(1,11) :
    entro = int(input('enter number:'))
    number.append(entro)
    sum_ = sum_ + entro
    tool = len(number)
avg =  sum_ / tool
print(f' list of number you enter : {number}')
print( f' avg of  list you enter : {avg} ')
