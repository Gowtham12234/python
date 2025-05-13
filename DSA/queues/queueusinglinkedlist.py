class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.length=0
    
    def enqueue(self,element):
        newnode=node(element)
        if self.rear is None:
            self.front=self.rear=newnode
            self.length+=1
            return
        self.rear.next=newnode
        self.rear=newnode
        self.length+=1

    def dequeue(self):
        if self.isempty():
            return "queuq is empty"
        delitem=self.front
        self.front=self.front.next
        self.length-=1
        if self.front is None:
            self.rear=None
        return delitem.value
    
    def isempty(self):
        return self.length==0
    
    def peek(self):
        if self.isempty():
            return "stack is empty"
        return self.front.value
    def printqueue(self):
        temp=self.front
        while temp:
            print(temp.value,end=" ")
            temp =temp.next
        print()
    
items=queue()

ele =list(input().split(","))

for e in ele:
    items.enqueue(e)

print("queue elements are ")
items.printqueue()
print("poped queue elements are ",items.dequeue())
print("elements after poping :")
items.printqueue()
print("peek",items.peek())
