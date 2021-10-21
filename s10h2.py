#ATEFE-JELVE__THURSDAY14-18
#CLASS_HOSPITAL
class Hospital:
    def __init__(self,docter,patient,room,hospitalization) :
        self.docter = docter
        self.patient = patient
        self.room = room
        self.hospitalization = hospitalization  # active
        self.capacity_now = 0

    def hospitalization_in(self,capacity):
        capacity_max =self.capacity_now + capacity
        if capacity_max>4:
            print('this room is full select another room')
        else:
            self.capacity_now+=capacity



register = Hospital('Key','Atefe' ,12 , 'active') 

register.hospitalization_in(1)
print(f'{register.capacity_now} person is in room\n')
register.hospitalization_in(1)
print(f'{register.capacity_now} person is in room\n')
register.hospitalization_in(1)
print(f'{register.capacity_now} person is in room\n')
register.hospitalization_in(1)
print(f'{register.capacity_now} person is in room\n')
register.hospitalization_in(1)
print(f'{register.capacity_now} person is in room\n')
register.hospitalization_in(1)
print(f'{register.capacity_now} person is in room\n')