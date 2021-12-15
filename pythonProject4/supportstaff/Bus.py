class Bus:
    """– This class displays the details of the bus for each area and also the driver
     details for a particular bus and the areas visited by the bus. """
    def __init__(self,busid,driver_name,totalseats,availibility):
        self.busid=busid
        self.driver=driver_name
        self.total=totalseats
        self.availibility=availibility
    def busDetails(self):
        print(f"bus id:{self.busid},driver name:{self.driver},total seats of bus:{self.total}")
    def seatsAvailability(self):
        if self.availibility:
            print("You can sit")
        else:
            print("You must stand on foot")
# bus111=Bus(111,"Ilqar",27,False)
# print(Bus.__doc__)
# bus136.busDetails()
# bus136.seatsAvailability()