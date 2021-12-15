from SchoolManagment import SchoolManagment
from room.classroom import Classroom
from supportstaff.manager import Manager
from Student.student import Student
from Student.HigherSecondaryStudent import HigherSecondaryStudent
from supportstaff.Department import Department
from Employee.Teacher import Teacher
from Employee.SupportStaff import SupportStaff
from supportstaff.Bus import Bus
from NoticeBoard import NoticeBoard
from other_room.Lab import Lab
from Equipment.Equipment import Equipment
from other_room.Auditorium import Auditorium
from SchoolArea import SchoolArea
from room.Notebook_room import Notebook_room
from room.Desktop_room import Desktop_room
from room.teacherroom import Teacherroom
from room.exam_room import Exam_Room
from other_room.library import Library
from room.Canteen import Canteen
from other_room.Shop import Shop
from other_room.Wc_for_men import Wc_for_men
from supportstaff.School_check_temperatue import Corona_check



print("********************************     School Detail     *******************************")
m1=SchoolManagment("Elsevar's School","Nefciler","0702334457","all")

print(m1.SchoolDetails())
m1.isOpen()

print("********************************       Schoolarea      ************************************")
sa1=SchoolArea(1500,1100)
l=sa1.getlength()
w=sa1.getweight()
print(f"weight:{w}m")
print(f"length:{l}m")
print(f"area:{sa1.area()}m")

print("**********************************    class detail     ************************************")
c1=Classroom("111","2a","123")
c1.ClassDetails()
print(c1.ClassDetails())
c2=Classroom("222","7b","124")
c2.ClassDetails()
print(c2.ClassDetails())
c3=Classroom("333","10a","125")
c3.ClassDetails()
print(c3.ClassDetails())


print("***********************************     student detail      *****************************")
print("*******primary student detail******")
ps1=Student("1","Elsevar","111","2",11)
ps2=Student("2","Nicat","111","2",11)
ps3=Student("3","Tural","111","2",11)
pd4=Student("4","azer","112","1",11)

print(ps1.StudentDetails())
print(ps2.StudentDetails())
print(ps3.StudentDetails())



print("*******  higher Secondary Student detail  ********")
hss1=HigherSecondaryStudent("111","Resad","333","4","33")
hss2=HigherSecondaryStudent("112","Derya","333","2","33")
hss1.HigherSecondaryStudentDetails()
hss2.HigherSecondaryStudentDetails()
print(hss1.HigherSecondaryStudentDetails())
print(hss2.HigherSecondaryStudentDetails())
print("***********************   to include students in the class   ******************")
man1=Manager("Vefa","Salamov",20,3000)

man1.manager_add(ps1,c1)
man1.manager_add(ps2,c1)
man1.manager_add(ps3,c1)
man1.manager_add(hss2,c2)
man1.manager_add(hss1,c3)
print("*******  the meneger add student in class  ******")

print("******************************           Department Detail       ******************")
d1=Department("dep1","English","Director")
d2=Department("dep2","Fars","Fexrende")
d1.DepartmentDetails()
d2.DepartmentDetails()
print(d1.DepartmentDetails())
print(d2.DepartmentDetails())
print("******************************         teacher      **********************")
t1=Teacher("E1","Emin","3200","English",1)
t1.show()

print(t1.Teacherdetail())
t1.CheckIn()
print("**************************                 SupporStaff      *****************")
ss1=SupportStaff("E3","Arzu","1600","English",8)

print(ss1.SupportStaffdetail())
ss1.CheckIn()

print("***********************                  bus                 *****************************")
bus11=Bus(11,"Elsever",25,False)
print(Bus.__doc__)
bus11.busDetails()
bus11.seatsAvailability()
bus33=Bus(33,"Samil",30,True)

bus33.busDetails()
bus33.seatsAvailability()
print("**********************               NoticeBoard     ***********************************")


n1=NoticeBoard()
print(n1.__doc__)
n1.AddContent("sa")
n1.AddContent("as")
n1.AddContent("assasld")
print(n1.Display())
print("*************************               Lab              ******************************")
l1=Lab("23","emin","235",True)
print(l1.__doc__)
print(l1.LabDetails())
l1.IsOccupied()
l2=Lab("234","else","32",False)
print(l1.LabDetails())
l1.IsOccupied()
print("***********************                ClassEquipment            ****************************")
ce1=Equipment("E1",21,"fan",2)
print(ce1.EquipmentDetails())
ce1.Repair()
ce2=Equipment("E2",10,"light",1)
print(ce2.EquipmentDetails())
ce2.Repair()
print("************************               LabEquipment             **********************")
le1=Equipment("L1",200,"Pipe",1)
print(le1.EquipmentDetails())
le1.Repair()
le2=Equipment("L2",100,"alcohol bank",6)
print(le2.EquipmentDetails())
le2.Repair()
print("*************************           Auditoruim          *************************")
A1=Auditorium(300,150,"new year","31.12.2021","06:00")
print(A1.EventDetails())
print(A1.DisplaySeats())
A1.Auditorium()
print("********************               Desktop_pc_room             ****************************")
Dpcroom1=Desktop_room("MSI",30,3200,True)
print(Dpcroom1.PC_detail())
Dpcroom1.Pc_room_full_or_not()

print("*********************             Notebook_pc_room           ************************")
npcroom1=Notebook_room("asus",30,3200,True,40)
print(npcroom1.PC_detail())
npcroom1.Pc_room_full_or_not()
npcroom1.Battery_check()
npcroom1.work_time2()
print("*******************                 Teacher_room             *************************")
teacher_room1=Teacherroom(30,True,"Vefa")
print(teacher_room1.Room_detail())
teacher_room1.teacher_isFull_or_not()

print("*******************                Exam_room                  ******************************")
exam_room1=Exam_Room(30,"10.04.2021",True,312)
print(exam_room1.Exam_room_detail())
exam_room1.Exam_room_is_Full_or_not()

exam_room1.Exam_date_add("20.10.2021")

exam_room1.Exam_date_add("25.11.2022")

exam_room1.Exam_date_add("10.5.2019")
print(exam_room1.Exam_date_display())
print("*****************                   Library                  ****************************")
l1=Library("Bextiyar Vahabzade","Elsevar",True,31,32)
l1.Isfull()
print(l1.Library_Detail())
l1.Book_is_full()

l2=Library("Keramet Boyukcol","Axundov",False,36,32)
l2.Isfull()
print(l2.Library_Detail())
l2.Book_is_full()

print("***************                     Canteen              *********************")
canteen1=Canteen(["shaurma","cay","kofe","bizon"],[5.4,2,4,10],300,[4,1,2,5],200,"Elsever's canteen")
print(canteen1.canteen_detail())
print(canteen1.display_items())
print(canteen1.is_available_items())
canteen1.is_available()
print("**********************              Shop                ***************************************")
shop1=Shop("Elsevar's shop",["pencil","book","copybook"],[1,3,2],[10,4,6])
print(shop1.Shop_detail())
print(shop1.display_items())
print("****************************           WC_for_men               ***********************************")
Wc_for_men1=Wc_for_men(True)
Wc_for_men1.isfull_or_not()
print("****************************             WC_for_womem         ***************************************")
Wc_for_women1=Wc_for_men(False)
Wc_for_women1.isfull_or_not()
print("************************             Check_temperauture            ***************************")
temperature=Corona_check(38)
temperature.check_temperature()