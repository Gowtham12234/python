r=4
n=r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for j in range(temp):
        print("*",end="")
    print()
for i in range(r):
    
    for j in range(i):
        print(" ",end="")
    temp1=2*r-1-(2*i)
    for k in range(temp1):
        print("*",end="")
    print()