class SchoolArea:
    def __init__(self,weight,length):
        self.weight=weight
        self.length=length

    def setweight(self,weight):
        self.weight=weight

    def getweight(self):
        return self.weight

    def setlength(self,length):
        self.length

    def getlength(self):
        return self.length

    def area(self):
        return self.length*self.weight



# sa1=SchoolArea(1500,1100)
# l=sa1.getlength()
# w=sa1.getweight()
# print(f"weight:{w}m")
# print(f"length:{l}m")
# print(f"area:{sa1.area()}m")