class Library:
    def __init__(self,Book_Name,Library_Name,Book_Num,Library_Seat,number_of_seats):
        self.Book_Name=Book_Name
        self.Book_Num=Book_Num
        self.Library_Name=Library_Name
        self.Library_Seat=Library_Seat
        self.number_of_seats=number_of_seats
    def Library_Detail(self):
        return f"this library is name {self.Library_Name},this library is consist of {self.Library_Seat} seats "

    def Isfull(self):
        if(self.Library_Seat<self.number_of_seats):
            print("this library seat is full")
        else:
            print(f"this library seat is empty and number of seats {self.number_of_seats}")
    def Book_is_full(self):
        if(self.Book_Num==1):
            print(f"this book is name {self.Book_Name} and  is full")
        else:
            print(f"this book is name {self.Book_Name}  and is empty")

# l1=Library("Bextiyar Vahabzade","Elsevar",True,31,32)
# l1.Isfull()
# print(l1.Library_Detail())
# l1.Book_is_full()
