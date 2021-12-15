from other_room.Wc import Wc
class Wc_for_men(Wc):
    def __init__(self,Isfull):
        super(Wc_for_men, self).__init__(Isfull)

    def isfull_or_not(self):
        if (self.Isfull == 1):
            print("this wc for men is full")
        else:
            print("this wc  for men is not full")
