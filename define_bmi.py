#ATEFE-JELVE__THURSDAY14-18
#DEFINE-BMI
def bmi(w,h):
    bmi = weight / ((height/100)**2)
    print(bmi)
    if bmi<=18.5 :
        print('UNDERWEIGHT')
    elif bmi>18.5 and bmi<=25 :
        print('NORMAL')
    elif bmi>=25 and bmi<=30 :
        print('OVERWEIGHT')
    elif bmi>=30 and bmi<=35 :
        print('OBESE')
    else:
        print('EXTREMLY OBESE')

weight = float(input('please enter your weight (kg):\n'))
height = float(input('please enter your height (cm):\n'))

bmi(weight,height)
