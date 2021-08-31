#ATEFE-JELVE__THURSDAY14-18
#DEFINE-BMI
def bmi(weight,height):
    bmi = weight / ((height/100)**2)
    print(f' YOUR BMI IS : {bmi}')
    if bmi<=18.5 :
        print('IT IS "UNDERWEIGHT"')
    elif bmi>18.5 and bmi<=25 :
        print('IT IS "NORMAL"')
    elif bmi>25 and bmi<=30 :
        print('IT IS "OVERWEIGHT"')
    elif bmi>30 and bmi<=35 :
        print('IT IS "OBESE"')
    else:
        print('IT IS "EXTREMLY OBESE"')

weight = float(input('please enter your weight (kg):\n'))
height = float(input('please enter your height (cm):\n'))

bmi(weight,height)
