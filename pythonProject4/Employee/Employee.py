from SchoolManagment import SchoolManagment
class Employee:


    def __init__(self,EmployeeId, EmployeeName, Salary, DepartmentId,watch_logged):
        self.EmployeeName=EmployeeName
        self.EmployeeId=EmployeeId
        self.Salary=Salary
        self.departmentId=DepartmentId
        self.watch_logged=watch_logged

    def CheckIn(self):
        if(self.watch_logged>7 and self.watch_logged<16):
            print("is school")
        else:
            print("is not school")




    def ReceiveSalary(self,is_salary):
        if(is_salary==True):
            print("teacher has recieve money")
        else:
            print("teacher has'n recieve money")




