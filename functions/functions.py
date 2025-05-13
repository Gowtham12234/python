def greet():
    print("hello")
greet()

def hello(name,age):
    print(f"hii my name is {name},and ia m {age} old")
hello("gowtham",19)

#positional arguments
def fullname(first,last):
    print(f"fullname:{first}{last}")
fullname("gowtham ","boyina")

#default arguments
def desham(country="india"):
    print(f"desham:{country}")
desham()# if we pass any name then it gets printed in this function

#keyword argumets
def details(age,name,course):
    print(f"name:{name} age {age} course: {course}")
details(age=19,name="gowtham",course="btech")

#arbitary arguments(*args,*kwargs):
#1.args
def snumbers(*numbers):
    total=sum(numbers)
    print(f"sum:{total}")
snumbers(1,2,4,3,5)
#2.kwargs
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
display_info(name="Vasanta", age=24, city="Chennai")

#return values using return statements
def square(num):
    return num*num
result=square(105)
print(result)