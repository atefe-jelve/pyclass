#ATEFE-JELVE__THURSDAY14-18
#CLASS_UNIVERCITY

class University:
    def __init__(self,student,course_code,teacher) :
        self.student = student
        self.course_code = course_code
        self.teacher= teacher

register = University('Atefe-Jelveh', 'Soft-Ware' ,'R.keshavarz')   
print(f' student name :\t"{register.student}" \n register in course code : "{register.course_code}" \n teacher name :\t "{register.teacher}" ')


