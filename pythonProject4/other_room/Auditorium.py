class Auditorium:
    def __init__(self,TotalSeats, SeatsOccupied, EventName, EventDate, EventTime):
        self.TotalSeats=TotalSeats
        self.SeatsOccupied=SeatsOccupied
        self.EventName=EventName
        self.EventDate=EventDate
        self.EventTime=EventTime
    def EventDetails(self):
        return f"There will be a New Year's party for {self.SeatsOccupied} people in the hall on the {self.EventDate} st of the month at {self.EventTime} o'clock"

    def DisplaySeats(self):
        return f"There are {self.TotalSeats} seats in the auditorium for any event"
    def Auditorium(self):
        if(self.EventDate !=None):
            print("tetbir var")
        else:
            print("bosdu")


# A1=Auditorium(300,150,"new year","31.12.2021","06:00")
# print(A1.EventDetails())
# print(A1.DisplaySeats())
# A1.Auditorium()