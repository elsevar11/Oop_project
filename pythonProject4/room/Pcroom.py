class Pcroom:
    def __init__(self,Pc_Model,Pc_Num,Pc_Price,Isfull):
        self.Pc_Model=Pc_Model
        self.Pc_Num=Pc_Num
        self.Pc_Price=Pc_Price
        self.Isfull=Isfull


    def PC_detail(self):
        return f"This pc Model is {self.Pc_Model},price is {self.Pc_Price}"


    def Pc_room_full_or_not(self):
        if(self.Isfull==1):
            print("pc room is full")
        else:
            print("pc room is empty")
    #composition
    def work_time(self):
        print('this pc working')

# pcroom1=Pcroom("asus",30,3200,True)
# print(pcroom1.PC_detail())
# pcroom1.Pc_room_full_or_not()