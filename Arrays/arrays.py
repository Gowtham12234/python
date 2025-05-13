#array creation 

fruits=["apple","mango","orange","plum"]

#accesing elements
x=fruits[0]
print(x)

#modify value 
fruits[2]="banana"
print(fruits)

#looping in arrays

for x in fruits:
    print(x)

#inserting elements At a specified index
fruits.insert(0,"guava")

#addin an element in array 

fruits.append("cashew")
print(fruits)

# #removig an element 

fruits.pop(3)
print(fruits)


#copying array into Another Arrays
tropicals=fruits.copy()
print(tropicals)


#clearing list
tropicals.clear()
print(tropicals)
print(fruits)
