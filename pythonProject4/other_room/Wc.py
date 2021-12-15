class Wc:
    def __init__(self,Isfull):
        self.Isfull=Isfull
    def isfull_or_not(self):
        if(self.Isfull==1):
            print("this wc is full")
        else:
            print("this wc is not full")
