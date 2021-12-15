from SchoolManagment import SchoolManagment
from Employee.Employee import Employee
class Teacher(Employee):
    def __init__(self, EmployeeId, EmployeeName, Salary, DepartmentId,watch_logged):
            super(Teacher,self).__init__( EmployeeId, EmployeeName, Salary, DepartmentId,watch_logged)

    def Teacherdetail(self):
        return f"bu Melliminn adi {self.EmployeeName} id ise {self.EmployeeId} ve bu maasi {self.Salary} department ise {self.departmentId}"

    def CheckIn(self):
        if(self.watch_logged>7 and self.watch_logged<16):
            print("at school")
        else:
            print("is not at school")
    def show(self):
    # The try block will raise an error when trying to write to a read-only file:
        try:
            f = open("../sa.txt", "a")
            try:
                f.write("Lorum Ipsum")
                print("no error")
            except:
                print("Something went wrong when writing to the file")
            finally:
                f.close()
        except:
            print("Something went wrong when opening the file")