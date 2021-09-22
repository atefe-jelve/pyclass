#ATEFE-JELVE__THURSDAY14-18
#DEFINE-AVG-NUMBERS-ENTER-BY-USER
number = list()
def num() :
    for i in range(1,11) :
        entro = int(input('enter number:'))
        number.append(entro)
    return number

def avg_() :
    sum_ = sum(number)
    tool = len(number)
    avg =  sum_ / tool
    return avg

result_num = num()
result = avg_()
print(f' list of number you enter : {result_num}')
print( f' avg of  list you enter : {result} ')
