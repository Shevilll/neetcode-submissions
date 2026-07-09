from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x: int) -> None:
        self.q1.append(x)

        while self.q2:
            self.q1.append(self.q2.popleft())


        self.q2, self.q1 = self.q1, self.q2    
       
        
        

    def pop(self) -> int:
        return self.q2.popleft()
        
        

    def top(self) -> int:
        return self.q2[0]
       
    def empty(self) -> bool:
        return len(self.q2) == 0
        
        






























# from collections import deque
# class MyStack:

#     def __init__(self):
#         self.q = deque()
    
#     def push(self, x: int) -> None:
#         self.q.append(x)
        

#     def pop(self) -> int:
#         for i in range (len(self.q) -1):
#             self.push(self.q.popleft())

#         return self.q.popleft()    

        

#     def top(self) -> int:
#         return self.q[-1]

#     def empty(self) -> bool:
#         return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()