#ATEFE-JELVE_THURSDAY_14-18
#DEFINE-volume-Or-Area-For-Geometric-SHapes-whit-return

def sphere(Radius):
    area = 4*pi*(Radius**2)
    return area
    volume = (4/3)*pi*(Radius**3)
    return volume

def cube(side):
    area = 6*(side**3)
    return area
    volume = (side**3)
    return volume

def print_shape(result):
    if calc.lower() == 'volume':
        print(f' the shape is: "" {shape.lower()} "" and the volume is: "" {result} "" ')
    elif calc.lower() == 'area':
        print(f' the shape is: "" {shape.lower()} " " and the area is : "" {result} "" ')
    else:
        print(f' the "" {calc} "" is wrong!!  please try again')

############################################################
shape = (input( 'hi guys!!! \n tell me  that Which of these \
shapes do you want me to calculate?:\n \
""cube"" or ""sphere""  \n\n\n '))

if shape.lower() == 'cube':
    side = int(input('enter one of side :'))
    calc = (input('enter you want calc """volume"" or ""Area"":'))
    result = cube(side)
    print_shape(result)

elif shape.lower() == 'sphere':
    Radius = int(input('enter one of Radius :'))
    calc = (input('enter you want calc """volume"" or ""Area"":'))
    pi=3.14
    result = sphere(Radius)
    print_shape(result)
