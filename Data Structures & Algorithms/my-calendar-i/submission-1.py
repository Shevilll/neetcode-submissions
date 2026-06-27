class MyCalendar:
    
    def __init__(self):
        self.arr = []
        self.n = 0

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(self.n):
            if self.arr[i][0] < endTime and startTime < self.arr[i][1]:
                return False
        
        self.arr.append([startTime, endTime])
        self.n += 1
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)