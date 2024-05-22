class node():
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

class linkedlist():
    def __init__(self):
        self.head=None
        self.tail=None
        
    def append(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
    
    def prepend(self,value):
        new_node=node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            new_node=self.head
            
    def delete(self,value):
        cur=self.head
        
        while cur:
            if cur.value==value:
                if cur.prev:
                    cur.prev.next=cur.next
                if cur.next:
                    cur.next.prev=cur.prev
                if cur==self.head:
                    self.head=cur.next
                if cur==self.tail:
                    self.tail=cur.prev
                return
            cur=cur.next
            
    def display_forward(self):
        cur = self.head
        while cur:
            print(cur.value, end=" <-> ")
            cur = cur.next
        print("None")

    def display_backward(self):
        cur = self.tail
        while cur:
            print(cur.value, end=" <-> ")
            cur = cur.prev
        print("None")
        
# Create a new linked list
dll = linkedlist()

# Append some elements
dll.append(1)
dll.append(2)
dll.append(3)

# Prepend some elements
dll.prepend(0)
dll.prepend(-1)

# Display the list forward and backward
print("Display forward:")
dll.display_forward()

print("Display backward:")
dll.display_backward()

# Delete an element
dll.delete(2)

# Display the list again to see the changes
print("Display forward after deleting 2:")
dll.display_forward()

print("Display backward after deleting 2:")
dll.display_backward()
