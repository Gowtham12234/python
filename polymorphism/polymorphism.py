#BASIC POLYMORPHISM
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("DRIVE")

class boat:
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print("sail ")
class plane():
    def __init__(self,model,brand):
        self.model=model
        self.brand=brand
    def move(self):
        print("fly ")
car1=car("toyato","fortunerr")
boat1=boat("ibizzaa","touring")
plane1=plane("boeing","852")

for x in (car1,boat1,plane1):
    x.move()