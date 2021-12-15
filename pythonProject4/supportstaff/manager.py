class Manager:
    def __init__(self,name,lastname,age,salary):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.salary=salary



    def manager_add(self,child,Class):
        if(len(Class.studentlist)<2):
           Class.studentlist.append(child)
           print(f"##the addition was successful##{Class.ClassId}")
        else:
            print(f"bu {Class.ClassId}id li sinif  doldu")




