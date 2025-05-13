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
node2.next=node3
node3.next=node4
node4.next=node1

currentnode=node1
startnode=node1
print(currentnode.data,end="->")
currentnode=currentnode.next

while currentnode!= startnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
print("...")
        