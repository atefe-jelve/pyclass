#ATEFE-JELVE_THURSDAY_14-18
#DEFINE-CALCULATE_ENTER_2_NUMBER_1_OPRERAOTR_WHIT_RETURN
def calc(frst_num,scnd_num,oprtr):
    if operator == '+' :
        result = first+secend
        return result
    elif operator == '-' :
        result = first-secend
        return result
    elif operator == '*' :
        result = first*secend
        return result
    elif operator == '/' :
        result = first/secend
        return result
    elif operator == '**' :
        result = first**secend
        return result
    elif operator == '//' :
        result = first//secend
        return result
    elif operator == '%' :
        result = first%secend
        return result
    else:
        print(f' operator : "" {operator} "" is wrong !! \n please try again !!')

def print_calc(result):
        print(f' the result is: {result}')

first = float(input('please enter first number:\n'))
secend = float(input('please enter secend number:\n'))
operator = (input('please enter operator:(+ , - , * , /, ** , // or %)\n'))

result = calc(first,secend,operator)
print_calc(result)
