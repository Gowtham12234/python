class queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isempty():
            return "queue is empty"
        return self.queue[0]
    
    def isempty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
items=queue()

ele =list(input().split(","))

for e in ele:
    items.enqueue(e)

print("queue elements are ",items.queue)
print("poped queue elements are ",items.dequeue())
print("peek",items.peek())
