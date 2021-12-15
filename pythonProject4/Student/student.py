class Student:
    def __init__(self,StudentId,StudentName,ClassId,Section,BusId):
        self.__StudentId=StudentId
        self.__StudentName=StudentName
        self.__ClassId=ClassId
        self.__Section=Section
        self.__BusId=BusId
    def StudentDetails(self):
        return f"bu sagirdin adi {self.StudentName} id ise {self.StudentId} ve bu sinife aiddi {self.ClassId}"

    # def get_StudentId(self):
    #     return self.__StudentId
    # def set_StudentId(self,StudentId):
    #     self.__StudentId=StudentId
    # def PayFees(self):
    #     pass
    @property
    def StudentId(self):
        return self.__StudentId

    @property
    def StudentName(self):
        return self.__StudentName

    @property
    def ClassId(self):
        return self.__ClassId

    @property
    def Section(self):
        return self.__Section

    @property
    def BusID(self):
        return self.__BusId

    @StudentId.setter
    def price(self, StudentID):
        self._StudentId = StudentID

    @StudentName.setter
    def color(self, StudentName):
        self._StudentName = StudentName

    @ClassId.setter
    def weight(self, ClassId):
        self._ClassId = ClassId

    @Section.setter
    def Section(self,Section):
        self._Section=Section

    @BusID.setter
    def BusId(self,BusId):
        self._BusId=BusId

    def __str__(self):
        return "Student Id=" + str(self.__StudentId) + "Student Name=" + str(self.__StudentName)+ "Class ID=" + str(self.__ClassId) +"Section=" + str(self.__Section)+"Bus  Id=" + str(self.__BusId)





# s1=Student("3452","elsever","123","fizika","hjf")
# s1.StudentDetails()
# print(s1.StudentDetails())


