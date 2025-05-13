# creation of class

class car:
    brand= "mahindhra"

#crateing object of the car class
car1=car()
print(car1.brand)

#using __init__

class cars:
    def __init__(self,brand,model):
        self.brand=brand #instance variable
        self.model=model #instane variable 

    #using __str__()function to print obj

    def __str__(self):
        return f"{self.brand}{self.model}"
        
car1=cars("toyota","fortunner")
car2=cars("mg","hector")
print(car1.brand ,car1.model) 
print(car2.brand,car2.model)

#by using __str__()function we can print the object which is represented in string ..

print(car1)     
