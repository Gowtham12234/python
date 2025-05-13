#singly linked list...

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=node(3)
node2=node(5)
node3=node(13)
node4=node(2)

node1.next=node2
node2.next=node3
node3.next=node4 

currentnode=node1
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
print("null")