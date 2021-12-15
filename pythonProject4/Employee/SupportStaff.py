from Employee.Employee import Employee


class SupportStaff(Employee):
    def __init__(self, EmployeeId, EmployeeName, Salary, DepartmentId,watch_logged):
        super(SupportStaff, self).__init__(EmployeeId, EmployeeName, Salary, DepartmentId,watch_logged)

    def SupportStaffdetail(self):
        return f"bu iscinin adi {self.EmployeeName} id ise {self.EmployeeId} ve bu maasi {self.Salary} department ise {self.departmentId}"
    def CheckIn(self):
        if(self.watch_logged>7 and self.watch_logged<16):
            print("at school")
        else:
            print("is not at school")