# doubly linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
node1=node(3)
node2=node(5)
node3=node(13)
node4=node(2)

node1.next=node2

node2.prev=node1
node2.next=node3

node3.prev=node2
node3.next=node4

node4.prev=node3

print("\n travesing forward")
currentnode=node1
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
print("null")

print("/n traversing from backward")
currentnode=node4
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.prev
print("null")
