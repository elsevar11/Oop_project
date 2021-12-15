class Department:
    def __init__(self,DepartmentId, DepartmentName, MemberList ):
        self.DepartmentId=DepartmentId
        self.DepartmentName=DepartmentName

        self.MemberList=MemberList
    def DepartmentDetails(self):
        return f"bu departmentin adi {self.DepartmentName} id ise {self.DepartmentId} ve bu memberi {self.MemberList}"
# d1=Department("dep1","English","Vefa")
# d2=Department("dep2","Fars","Fexrende")
# d1.DepartmentDetails()
# d2.DepartmentDetails()
# print(d1.DepartmentDetails())
# print(d2.DepartmentDetails())