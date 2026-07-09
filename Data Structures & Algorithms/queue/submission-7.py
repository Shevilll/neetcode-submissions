from collections import deque

class Deque:
    
    def __init__(self):
        self.queue = deque()


    def isEmpty(self) -> bool:
        return len(self.queue) == 0
        

    def append(self, value: int) -> None:
        self.queue.append(value)

        

    def appendleft(self, value: int) -> None:
        
            self.queue.appendleft(value)
    
        

    def pop(self) -> int:
        if len(self.queue) == 0:
            return -1
        else:  
            return self.queue.pop() 
        
        

    def popleft(self) -> int:

        if len(self.queue) == 0:
             return -1

        else:  
            return self.queue.popleft()   

        
        
