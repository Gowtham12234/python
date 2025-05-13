class node:
    def __init__(self,value):
        self.value=value
        self.size=0

class stack:
    def __init__(self):
        self.head=None
        self.size=0

    def push(self,value):
        newnode=node(value)
        newnode.next=self.head
        self.head=newnode
        self.size+=1

    def pop(self):
        if self.isempty():
            return "stack is empty"
        poped_value=self.head
        self.head=self.head.next
        self.size -=1
        return poped_value.value

    def peek(self):
        if self.isempty():
            return "stack is empty"
        return self.head.value
    
    def isempty(self):
        return self.size == 0
    
    
    def stacksize(self):
        return self.size
    
mystack=stack()

values=list(input().split(","))

for i in values:
    mystack.push(i)


print("pop:",mystack.pop())
print("peek:",mystack.peek())
print("is empty",mystack.isempty())
print("size:",mystack.stacksize())
