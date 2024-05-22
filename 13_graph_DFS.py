class node():
    def __init__(self,value):
        self.value=value
        self.adjacent_list=[]
        self.visited=False
        
class Graph():
    def DFS(self,start,traversal):
        node.visited=True
        traversal.append(start.value)
        
        for element in start.adjacent_list:
            if element.visited is False:
                 self.DFS(element,traversal)
        return traversal

node1 = node("A")
node2 = node("B")
node3 = node("C")
node4 = node("D")
node5 = node("E")
node6 = node("F")
node7 = node("G")

node1.adjacent_list.append(node2)
node1.adjacent_list.append(node3)
node1.adjacent_list.append(node4)
node2.adjacent_list.append(node5)
node2.adjacent_list.append(node6)
node4.adjacent_list.append(node7)

graph=Graph()
print(graph.DFS(node1,[]))        