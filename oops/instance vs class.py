class employee:
    company="hcl" # class varible 
    def __init__(self,name,salary):
        self.salary=salary  #instance variable
        self.name=name  #instance variable

emp1=employee("tim",150000)
emp2=employee("alex,",50000)
print(emp1.company)
print(emp2.company)

#changing class variable

employee.company="infosys"
print(emp1.company)
        