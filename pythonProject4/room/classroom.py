class Classroom:
    def __init__(self,ClassId,ClassName,TeacherId):
        self.ClassId=ClassId
        self.ClassName=ClassName
        self.TeacherId=TeacherId

        self.studentlist = list()
    def ClassDetails(self):
        return f"this class id is {self.ClassId}, name is {self.ClassName}"


# c1=Classroom("123","10b","321",30)
# c1.ClassDetails()
# print(c1.ClassDetails())