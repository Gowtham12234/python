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
def deletenode(head,nodedelete):
    if head==nodedelete:
        return head.next
    
    currentnode=head
    while currentnode and currentnode.next!=nodedelete:
        currentnode=currentnode.next
    if currentnode.next is None:
        return head
    
    currentnode.next=currentnode.next.next

    return head

node1 = node(7)
node2 = node(11)
node3 = node(3)
node4 = node(2)
node5 = node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("\n before traversing ")

traverseandprint(node1)

node1=deletenode(node1,node4)


print("\n after deletion")
traverseandprint(node1)