class node():
    def __init__(self,value):
        self.value=value
        self.adjacent_list=[]
        self.visited=False

class Graph():
    def bfs(self,value):
        queue=[]
        queue.append(value)
        node.visited=True
        
        traversal=[]
        while queue:
            actualNode=queue.pop(0)
            traversal.append(actualNode.value)
            
            for element in actualNode.adjacent_list:
                if element.visited is False:
                    queue.append(element)
                    element.visited= True
        return traversal
    
node1=node("A")
node2=node("B")
node3=node("C")
node4=node("D")
node5=node("E")
node6=node("F")
node7=node("G")
node8=node("H")

node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)
node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)
node4.adjacent_list.append(node7)
node6.adjacent_list.append(node8)

graph=Graph()
print(graph.bfs(node1))
        
        