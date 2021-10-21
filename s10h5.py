#ATEFE-JELVE__THURSDAY14-18
#CLASS_ELEVAYTOR

class Elevator:
    def __init__(self,door,floor,status_move) :
        self.door = door    # open or close
        self.floor = floor
        self.status_move = status_move # up or down


    def enter_key(self):
        print('the door is open come in please and enter  floor number :\n')
        if self.floor > 0 and self.status_move == 'down' :
            n=self.floor
            for i in range(n):
                print(f'floor {n}')
                n=n-1
            print('you are in grand floor\n your welcome')
        else:
            print('you are in 0 floor ')




run_elvtr = Elevator('open', 5, 'down')

run_elvtr.enter_key()