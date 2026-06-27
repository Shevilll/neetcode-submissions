class MyCalendar:
    
    def __init__(self):
        self.arr = []
        self.n = 0

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(self.n):
            if (startTime >= self.arr[i][0] and startTime >= self.arr[i][1]) and (endTime >= self.arr[i][0] and endTime >= self.arr[i][1]):
                self.n += 1
                self.arr.append([startTime, endTime])
                return True
            else:
                return False

        self.n += 1
        self.arr.append([startTime, endTime])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)