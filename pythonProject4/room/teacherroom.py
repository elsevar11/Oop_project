class Teacherroom:
    def __init__(self,TeacherNum,Teacher_isFull,Teacher_Name):
        self.Teachers_Name=Teacher_Name
        self.TeacherNum=TeacherNum
        self.Teacher_isFull=Teacher_isFull
    def Room_detail(self):
        return f"There are {self.TeacherNum} seats in the teachers' room"
    def teacher_isFull_or_not(self):
        if (self.Teacher_isFull == 1):
            print(f"{self.Teachers_Name} Teacher is full")
        else:
            print(f"{self.Teachers_Name} Teacher is empty")

