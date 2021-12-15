from Student.student import Student
class PrimaryStudent(Student):
    def __init__(self,StudentId,StudentName,ClassId,Section,BusId):
        super(PrimaryStudent, self).__init__(StudentId,StudentName,ClassId,Section,BusId)


    def PrimaryStudentDetails(self):
        return f"bu sagirdin adi {self.StudentName} id ise {self.StudentId} ve bu sinife aiddi {self.ClassId}"



    # def __init__(self,StudentId,StudentName,ClassId,Section,BusId):
    #     # self.__elavedil = elavedil
    #     Student.__init__(self,StudentId,StudentName,ClassId,Section,BusId)

    # def get_elavedil(self):
    #     return self.elavedil
    #
    # def set_elavedil(self, elavedil):
    #     self.elavedil = elavedil

    # def __str__(self):
    #     return super().__str__() + " elavedil " + str(self.elavedil())
# ps1=PrimaryStudent("8436","husikadeGF","123","ASUFI","asf")
# ps1.PrimaryStudentDetails()
# print(ps1.PrimaryStudentDetails())
# ps1=PrimaryStudent("21","elsa","fsf32",":asf","adsas")
# print(ps1)