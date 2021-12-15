from Student.student import Student
class HigherSecondaryStudent(Student):
    def __init__(self,StudentId,StudentName,ClassId,Section,BusId):
        super(HigherSecondaryStudent, self).__init__(StudentId,StudentName,ClassId,Section,BusId)

    def HigherSecondaryStudentDetails(self):
        return f"bu sagirdin adi {self.StudentName} id ise {self.StudentId} ve bu sinife aiddi {self.ClassId}"


# hss1=HigherSecondaryStudent("111","Resad","333","1group","33")
# hss1.HigherSecondaryStudentDetails()
# print(hss1.HigherSecondaryStudentDetails())