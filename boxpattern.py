r=4
c=4
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j!=c-1:
            print("-",end="")
    print()