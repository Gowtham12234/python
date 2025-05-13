class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,element):
        self.stack.append(element)

    def pop(self):
        if self.isempty():
            return "stack is"
        return self.stack.pop()
    
    def peek(self):
        if self.isempty():
            return "stack is empty"
        return self.stack[-1]
    
    def isempty(self):
        return len[stack] == 0
    
    def size(self):
        return len[stack]
    
    def __getitem__(self,index):
        return self.stack[index]
    

mystack=stack()

values=list(input().split(","))

for i in values:
    mystack.push(i)
    

print(mystack[2])


