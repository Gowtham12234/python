c=3
r=10
for i in range(r):
    for j in range(c):
        print("*",end="")
        if j!=c-1:
            print("-",end="")
    print()