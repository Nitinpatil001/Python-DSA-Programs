class node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.rigth=None
    
class binarytree():
    def __init__(self,value):
        self.root=node(value)
        
tree=binarytree(3)

tree.root.left=node(4)
tree.root.rigth=node(5)

tree.root.left.left=node(6)
tree.root.left.rigth=node(7)

tree.root.rigth.left=node(8)
tree.root.rigth.rigth=node(9)
        
    