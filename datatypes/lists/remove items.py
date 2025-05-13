list = ["apple", "banana", "cherry", "apple", "cherry"]
#remove function we can remove specified items

list.remove("banana")
print(list)

#pop() is used to delete a item at a certain index
list.pop(2)
print(list)

#del() is used to remove specified item and also it can delete whole list

del list[1]
print(list)

#clear() is used clear the existing list
list.clear()
print(list)

