class MyLinkedList: # manage  whole linked list

    class Node:

        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

        
           
        

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

        

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val         
        

    def addAtHead(self, val: int) -> None:
        new_node = self.Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1            
            
      

        

    def addAtTail(self, val: int) -> None:
        new_node = self.Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            curr = self.tail
           
            curr.next = new_node
            new_node.prev = curr
            self.tail = new_node    
        self.size += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 

        if index == 0:
            self.addAtHead(val)
            return    

        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.head
       

        for i in range(index):
            curr = curr.next

        new_node = self.Node(val)   

        prev_node = curr.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = curr
        curr.prev = new_node
        self.size += 1
   

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self. size:
            return 

        curr = self.head

        for i in range(index):
            curr = curr.next

        if curr.prev is not None:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next is not None:
            curr.next.prev = curr.prev

        else:
            self.tail = curr.prev

        self.size -= 1    
                    
                    

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)