#factorial program

def factorial(n):
    if n == 0 or n == 1:   #base case
        return True
    return n * factorial(n-1)# recursive case
print(factorial(10)) 


#fibanacci series 

def fibanacci(n):
    if n == 0:
        return False #base case
    elif n == 1:
        return True
    return fibanacci(n-1)+fibanacci(n-2)#recursive case
print(fibanacci(10))