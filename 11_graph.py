class node():
    def __init__(self,value):
        self.value=value
        self.adjacentlist=[]
        self.visited=False
    
node1=node("A")
node2=node("B")
node3=node("C")
node4=node("D")
node5=node("E")
node6=node("F")
node7=node("G")
node8=node("H")

node1.adjacentlist.append(node2)
node1.adjacentlist.append(node3)
node1.adjacentlist.append(node4)
node2.adjacentlist.append(node5)
node2.adjacentlist.append(node6)
node4.adjacentlist.append(node7)
node6.adjacentlist.append(node8)

