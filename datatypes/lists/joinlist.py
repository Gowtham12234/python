l=["hello","hii"]
l2=["name","fame"]
l3=[]
l4=[]
l3=l+l2
print(l3)

for x in l3:
    l4.append(x)
print(l4)
l5=["car","bike"]
l4.extend(l5)
print(l4)
print(l4.count("hello"))