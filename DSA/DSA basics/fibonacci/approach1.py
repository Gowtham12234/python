#create  the 20 first fibonacci numbers sing for loop....

num1=0
num2=1

#printing the first two numbers of the series
print(num1) 
print(num2)

#for loop for remaining numbers

for new in range(18):
    new=num1+num2
    print(new) #printing new number
    num1=num2  #incrementing 1st number to second number
    num2=new #incrementing 2nd number to newly generated value..

