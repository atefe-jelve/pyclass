#ATEFE-JELVE_THURSDAY_14-18
#DEFINE-Environment-Or-Area-For-Geometric-SHapes

shape = (input( 'hi guys!!! \n tell me  that Which of these \
shapes do you want me to calculate?:\n \
""Rectangle"" or ""Circle"" or ""Square"" or ""Triangle""\n\n\n '))
if shape.lower() == 'rectangle':
    def Rectangle(length,Width,calc):
        area = length*Width
        environment = (length+Width)*2
        if calc == 'environment':
            print(f' the shape is: "" {shape.lower()} "" and the environment is: "" {environment} "" ')
        elif calc == 'area':
            print(f' the shape is: "" {shape.lower()} " " and the area is : "" {area} "" ')
        else:
            print(f' the "" {calc} "" is wrong!!  please try again')
    length = int(input('enter length :'))
    Width = int(input('enter width:'))
    calc = (input('enter you want calc """Environment"" or ""Area"":'))
    Rectangle(length,Width,calc.lower())
elif shape.lower() == 'circle':
    def circle(Radius,calc):
        environment = 2*pi*Radius
        area = pi*(Radius**Radius)
        if calc == 'environment':
            print(f' the shape is: "" {shape.lower()} "" and the environment is: "" {environment} "" ')
        elif calc == 'area':
            print(f' the shape is: "" {shape.lower()} " " and the area is : "" {area} "" ')
        else:
            print(f' the "" {calc} "" is wrong!!  please try again')
    pi = 3.14
    Radius = int(input('enter number radius for circle :'))
    calc = (input('enter you want calc """Environment"" or ""Area"" :'))
    circle(Radius,calc.lower())
elif shape.lower() == 'triangle':
    calc = (input('enter you want calc """Environment"" or ""Area"" :'))
    calc = calc.lower()
    if calc == 'environment':
        def triangle_environment(side1,side2,side3):
            environment = (side1+side2+side3)
            print(f' the shape is: "" {shape.lower()} "" and the environment is: "" {environment} "" ')
        side1 = int(input('enter first The side of the triangle :'))
        side2 = int(input('enter secend The side of the triangle :'))
        side3 = int(input('enter third The side of the triangle :'))
        triangle_environment(side1,side2,side3)
    elif calc == 'area':
        def triangle_area(Base,Height):
            area = ((Base*Height)/2)
            print(f' the shape is: "" {shape.lower()} " " and the area is : "" {area} "" ')
    else:
        print(f' the "" {calc} "" is wrong!!  please try again')

        Base = int(input('enter Base of the triangle :'))
        Height = int(input('enter Height of the triangle :'))
        triangle_area(Base,Height)
elif shape.lower() == 'square':
    def Square(side,calc):
        environment = 4*side
        area = side*side
        if calc == 'environment':
            print(f' the shape is: "" {shape.lower()} "" and the environment is: "" {environment} "" ')
        elif calc == 'area':
            print(f' the shape is: "" {shape.lower()} " " and the area is : "" {area} "" ')
        else:
            print(f' the "" {calc} "" is wrong!!  please try again')
    side = int(input('enter number side for Square :'))
    calc = (input('enter you want calc """Environment"" or ""Area"" :'))
    Square(side,calc.lower())
else:
    print(f' ohh!! sorry!! the shape is wrong please try again')
