#ATEFE-JELVE__THURSDAY14-18
#DEFINE-BMI-WHIT-RETURN
def bmi_calc(weight,height):
    bmi = weight / ((height/100)**2)
    return bmi
    
def bmi_range(result):
    print(f' YOUR BMI IS : {result}')
    if result<=18.5 :
        print('IT IS "UNDERWEIGHT"')
    elif result>18.5 and result<=25 :
        print('IT IS "NORMAL"')
    elif result>25 and result<=30 :
        print('IT IS "OVERWEIGHT"')
    elif result>30 and result<=35 :
        print('IT IS "OBESE"')
    else:
        print('IT IS "EXTREMLY OBESE"')

weight = float(input('please enter your weight (kg):\n'))
height = float(input('please enter your height (cm):\n'))

result=bmi_calc(weight,height)
bmi_range(result)
