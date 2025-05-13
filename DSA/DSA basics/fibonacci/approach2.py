count=0
def fibanocci(num1,num2):                   #defining function with two arguments 
    global count                            #declaring global count because it si declared outside and used accesed in function
    if count<=20:
        new=num1+num2
        print(new)  
        num1=num2                           #incrementing num1 to num2
        num2=new                            #incrementing num2 to new 
        count+=1                            #incrementing the count so the loop move forward
        fibanocci(num1,num2)                # calling the fibanocci function (meeans recursive function),calling itself 
    else:
        return
    
fibanocci(0,1)