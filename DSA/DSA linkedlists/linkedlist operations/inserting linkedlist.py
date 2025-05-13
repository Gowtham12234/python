class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def traverseandprint(head):
    currentnode=head
    while currentnode:
        print(currentnode.data,end="->")
        currentnode=currentnode.next
    print("null")

def insertingnode(head,newnode,position):
    if position == 1:
        newnode.next=head
        return newnode
    currentnode=head
    for _ in range(position -2):
        if currentnode is None:
            break
        currentnode=currentnode.next

    newnode.next=currentnode.next  #new node points to 2 which is currentnode s next

    currentnode.next=newnode       #3 now points to newnode(97)
    return head


values =list(map(int,input().split(",")))
head=node(values[0])
currentnode=head
for val in values[1:]:
    newnode=node(val)
    currentnode.next=newnode
    currentnode=newnode
print("original list")
traverseandprint(head)

newval =int(input())
position=int(input())
newnode=node(newval)
head=insertingnode(head,newnode,position)
print("\n after traversal")
traverseandprint(head)
