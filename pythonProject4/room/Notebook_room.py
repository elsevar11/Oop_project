from room.Pcroom import Pcroom
class Notebook_room(Pcroom):
    def __init__(self,Pc_Model,Pc_Num,Pc_Price,Isfull,Battery):
        super(Notebook_room, self).__init__(Pc_Model,Pc_Num,Pc_Price,Isfull)
        self.Battery=Battery
        #composition
        self.obj1 = Pcroom("acer",2,12531,False)

        print('notebook room created')
       #composition
    def work_time2(self):

        print('class work_time2() method')
        self.obj1.work_time()
    def PC_detail(self):
        return f"This pc Model is {self.Pc_Model},price is {self.Pc_Price}"

    def Pc_room_full_or_not(self):
        if (self.Isfull == 1):
            print("pc room is full")
        else:
            print("pc room is empty")
    def Battery_check(self):
        if(self.Battery>30):
            print(f"this notebook can be work and battery is {self.Battery}")
        else:
            print(f"this notebook can not work and battery is {self.Battery}")

     # Polymorphism
        # Polymorphism
    def show(self):
            print("there are {} notebook pc".format(self.Pc_Num))


# obj=Notebook_room("asus",30,3200,True,40)
# obj.work_time2()
# obj.Pc_room_full_or_not()
# print(obj.PC_detail())