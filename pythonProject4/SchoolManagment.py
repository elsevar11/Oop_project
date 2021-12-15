from datetime import datetime
class SchoolManagment:

    def __init__(self,SchoolName,Address,ContactNumber,Mediumofstudy):
        self.SchoolName=SchoolName
        self.Address=Address
        self.ContactNumber=ContactNumber
        self.Mediumofstudy=Mediumofstudy
        self.saat=datetime.now().hour

    # def get_saat(self):
    #     return self.__saat
    # def set_saat(self,saat):
    #     self.__saat=saat

    def isOpen(self):
        if(self.saat>7 and self.saat<16):
            print(f"the school is open at {self.saat} p.m.")
        else:
            print(f"the school is close at {self.saat} p.m.")

    def SchoolDetails(self):
        return f"school name is {self.SchoolName} \naddress is {self.Address} \nContact number is {self.ContactNumber} ;"




# m1=SchoolManagment("elsever","nefciler","0555555555","sa",8)
# m1.isOpen()
#
# print(m1.saat)
# print(m1.SchoolDetails())
