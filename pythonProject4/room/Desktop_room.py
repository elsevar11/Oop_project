from room.Pcroom import Pcroom
class Desktop_room(Pcroom):
    def __init__(self,Pc_Model,Pc_Num,Pc_Price,Isfull):
        super(Desktop_room, self).__init__(Pc_Model,Pc_Num,Pc_Price,Isfull)

    def PC_detail(self):
        return f"This pc Model is {self.Pc_Model},price is {self.Pc_Price}"

    def Pc_room_full_or_not(self):
        if (self.Isfull == 1):
            print("pc room is full")
        else:
            print("pc room is empty")
    #Polymorphism
    def show(self):
        print("there are {} desktop pc".format(self.Pc_Num))