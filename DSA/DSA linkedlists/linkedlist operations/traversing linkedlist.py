class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traversalandprint(head):
    currentnode=head
    while currentnode:
        print(currentnode.data,end="->")
        currentnode=currentnode.next
    print("null")

node1=node(3)
node2=node(5)
node3=node(13)
node4=node(2)

node1.next=node2
node2.next=node3
node3.next=node4

traversalandprint(node1)

# finding lowest value in linked list

def lowestvalue(head):
    minvalue=head.data
    currentnode=head.next
    while currentnode:
        if currentnode.data<minvalue:
            minvalue=currentnode.data
        currentnode=currentnode.next
    return minvalue
print(lowestvalue(node1))