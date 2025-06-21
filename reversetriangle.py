r=4
n=r-1

for i in range(r):
    for l in range(n-i):
        print(" ",end="")
    temp=i*2+1
    for o in range(temp):
        print("*",end="")
    print()