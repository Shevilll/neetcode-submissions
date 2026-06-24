class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack == []:
            return False
        else:
            self.stack.pop()    
        
        

    def top(self) -> int:
        if self.stack == []:
            return False
        else:
            top_val = self.stack[-1]
            return top_val
        

        

    def getMin(self) -> int:

        min_stack = min(self.stack)
        return min_stack  

