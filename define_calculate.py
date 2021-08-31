#ATEFE-JELVE_THURSDAY_14-18
#DEFINE-CALCULATE_ENTER_2_NUMBER_1_OPRERAOTR
def calculator(frst_num,scnd_num,oprtr):
    if operator == '+' :
        print(first+secend)
    elif operator == '-' :
        print(first-secend)
    elif operator == '*' :
        print(first*secend)
    elif operator == '/' :
        print(first/secend)
    elif operator == '**' :
        print(first**secend)
    elif operator == '//' :
        print(first//secend)
    elif operator == '%' :
        print(first%secend)
    else:
        print('operator is wrong !! \n please try again !!')
first = float(input('please enter first number:\n'))
secend = float(input('please enter secend number:\n'))
operator = (input('please enter operator:(+ , - , * , /, ** , // or %)\n'))
calculator(first,secend,operator)
