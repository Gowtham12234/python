#create a parent class

class person:    #parent class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(self.fname,self.lname)
#use the person class to create an object ,and then execute the printname function

x=person("gowtham","boyina")
x.printname()

# child class

class student(person):   #child class

    pass # use pass to define that no additional functionalites rather than the functionlites in parent class

class employee(person):   #child class

    def __init__(self, fname, lname):  # used this method to skip the "pass" keyword 

        person.__init__(self,fname, lname)#used to call the parent __init__ function ,due to skipping of pass keyword

        self.salary=500000 # adding properties,

z=employee("jim","john")
print(z.salary) 
z.printname()

y=student("punith","boyina")
y.printname()