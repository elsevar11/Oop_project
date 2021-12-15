class Corona_check:
    def __init__(self,temperature):
        self.temperature=temperature
    def check_temperature(self):
        if(self.temperature<36.6):
            print(f"can be enter the school and temperature: {self.temperature}")
        else:
            print(f"can not enter the school and temperature: {self.temperature}")