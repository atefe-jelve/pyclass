#ATEFE-JELVE__THURSDAY14-18
#CLASS_GATE

class Gate:
    def __init__(self, status, user, code) :
        self.status = status  #log_in or exit 
        self.date_time = '00:00'
        self.user = user
        self.code = code


    def __str__(self): 
        return f'well come : {self.user} - {self.code}  '




a=Gate( 'log_in','Atefe', 1369)
print(a)