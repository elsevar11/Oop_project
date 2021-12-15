class Canteen:
    """This class is for storing Canteen details inside the school"""
    def __init__(self,items_list,Available_items_list,Available_seat,items_price,occupied_seat,canteen_name):
        self.canteen_name=canteen_name
        self.items_list=items_list
        self.Available_items_list=Available_items_list
        self.Available_seat=Available_seat
        self.items_price=items_price
        self.occupied_seat=occupied_seat
       # for i in items_list:
          #  self.items_list.append(i)

    def canteen_detail(self):
        return f"this canteen name is {self.canteen_name} and this canteen consist of {self.Available_seat} seats"
    def display_items(self):
        return f"There are these {self.items_list} items in the canteen and price is {self.items_price}"
    def is_available(self):
        if(self.Available_seat>self.occupied_seat):
            print("There is room to sit in the canteen")
        else:
            print("There is not  room to sit in the canteen")
    def is_available_items(self):
        return f"{self.Available_items_list} the number of these items in the canteen"

# canteen1=Canteen(["shaurma","cay","kofe","bizon"],[5.4,2,4,10],300,[4,1,2,5],200,"Elsever's canteen")
# print(canteen1.canteen_detail())
# print(canteen1.display_items())
# print(canteen1.is_available_items())
# canteen1.is_available()


