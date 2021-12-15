class Lab:
    """Lab – This

    class contains the lab details of any school with its necessary information."""
    def __init__(self,LabId,LabName,EquipmentId,isfull):
        self.LabId=LabId
        self.LabName=LabName
        self.EquipmentId=EquipmentId
        self.isfull=isfull
    def LabDetails(self):
        return f"this lab name is {self.LabName}, Id is {self.LabId}, the equipment id is {self.EquipmentId}"

    def IsOccupied(self):
        if(self.isfull==1):
            print("This lab is Occupied")
        else:
            print("this Lab is empty")



# l1=Lab("23","emin","235",False)
# print(l1.__doc__)
# print(l1.LabDetails())
# # l1.IsOccupied()
# print(l1.IsOccupied())