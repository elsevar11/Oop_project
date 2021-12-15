from other_room.Wc import Wc
class Wc_for_women(Wc):
    def __init__(self,Isfull):
        super(Wc_for_women, self).__init__(Isfull)

    def isfull_or_not(self):
        if (self.Isfull == 1):
            print("this wc for women is full")
        else:
            print("this wc for women  is not full")
