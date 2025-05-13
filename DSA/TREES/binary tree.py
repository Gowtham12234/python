class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=node('g')
node1=node("e")
node2=node('w')
node3=node('t')
node4=node("l")
node5=node("c")
node6=node('p')

root.left=node1
root.right=node2
node1.left=node3
node1.right=node4

node2.left=node5
node2.right=node6

def preordertraversal(node):
    if node is None:
        return
    print(f"{node.data} ",end=",")
    preordertraversal(node.left)
    preordertraversal(node.right)
print("preoder traversal:")
preordertraversal(root)

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(f"{node.data}",end=",")
    inorder(node.right)
print("\n inoder traversal:")
inorder(root)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data,end=",")
print("\n postorder traversal ")
postorder(root)