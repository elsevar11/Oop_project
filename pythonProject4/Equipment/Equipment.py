class Equipment:
    def __init__(self,EquipmentId,Cost,EquipmentName,work_time):
        self.EquipmentId=EquipmentId
        self.Cost=Cost
        self.EquipmentName=EquipmentName
        self.work_time=work_time
    def EquipmentDetails(self):
        return f"this equipment's name is {self.EquipmentName} id is {self.EquipmentId},the price is {self.Cost} work time {self.work_time}"


    def Repair(self):
        if(self.work_time>1):
            print("It had to be repaired with a new one for more than 1 year")
        else:
            print("There was no need for repairs for less than 1 year")


# e1=Equipment(1,21,"da",2)
# print(e1.EquipmentDetails())
# e1.Repair()
