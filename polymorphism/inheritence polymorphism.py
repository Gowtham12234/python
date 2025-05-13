class vehicle:
    def __init__(self,model,brand):
        self.model=model 
        self.brand=brand
    def move(self):
        print("driving mode")
class car(vehicle):
    pass
class boat(vehicle):
    def move(self):
        print("sailing mode ")

class plane(vehicle):
    def move(self):
        print("flying mode")

car1 = car("Ford", "Mustang")      
boat1 = boat("Ibiza", "Touring 20") 
plane1 = plane("Boeing", "747") 

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()