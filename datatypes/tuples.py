x=("apple","orange","cherry","mango","guava")
# print(x[0])
# print(x[1:3])
# print(x[:5])


#adding in tuple

y=list(x)
y.append("pulm")
x=tuple(y)
print(x)

for i in range(len(x)):
    print(x[i])
