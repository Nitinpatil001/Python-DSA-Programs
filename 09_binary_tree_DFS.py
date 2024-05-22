class node():
    def __init__(self,value):
        self.value=value
        self.left=None
        self.rigth=None

class binarytree():
    def __init__(self,value):
        self.root=node(value)
        
    def preorder(self,start,traversal):
        #root->left->rigth
        if start is None:
            return
        traversal.append(start.value)
        self.preorder(start.left,traversal)
        self.preorder(start.rigth,traversal)
        
        return traversal
    
    def inorder(self,start,traversal):
        #left->root->rigth
        if start is None:
            return
        self.inorder(start.left,traversal)
        traversal.append(start.value)
        self.inorder(start.rigth,traversal)
        
        return traversal
    
    def postorder(self,start,traversal):
        #left->rigth->root
        if start is None:
            return
        self.postorder(start.left,traversal)
        self.postorder(start.rigth,traversal)
        traversal.append(start.value)
        
        return traversal     
                        
tree = binarytree(3)

tree.root.left=node(4)
tree.root.left.left=node(5)
tree.root.left.rigth=node(6)

tree.root.rigth=node(7)
tree.root.rigth.left=node(8)
tree.root.rigth.rigth=node(9)

print(tree.preorder(tree.root,[]))
print(tree.inorder(tree.root,[]))
print(tree.postorder(tree.root,[]))