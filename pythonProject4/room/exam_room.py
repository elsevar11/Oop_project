class Exam_Room():
    def __init__(self,Seat_Num,Exam_Date,IsFull,Room_ID):
        self.Seat_Num=Seat_Num
        self.Exams_Date=list()
        self.IsFull=IsFull
        self.Room_ID=Room_ID
    def Exam_room_is_Full_or_not(self):
        if (self.IsFull == 1):
            print(f"there is an exam here {self.Room_ID} roomID")
        else:
            print(f"there is not an exam here {self.Room_ID} roomId")
    def Exam_room_detail(self):
        return f"this exam room is consist of {self.Seat_Num} seats and Room id is {self.Room_ID}"
    def Exam_date_add(self,Date):
        self.Exams_Date.append(Date)
    def Exam_date_display(self):
        return  f"there will be an exam on these dates :{self.Exams_Date}"


# exam_room1=Exam_Room(30,"10.04.2021",True,312)
# print(exam_room1.Exam_room_detail())
# exam_room1.Exam_room_is_Full_or_not()
#
# exam_room1.Exam_date_add("20.10.2021")
#
# exam_room1.Exam_date_add("25.11.2022")
#
# exam_room1.Exam_date_add("10.5.2019")
# print(exam_room1.Exam_date_display())
