class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None

    def append(self, value: int) -> None:
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
            return
        self.tail.next = ListNode(value)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        if not self.head:
            self.head = ListNode(value)
            self.tail = self.head
            return
        new = ListNode(value)
        new.next = self.head
        self.head.prev = new
        self.head = new

    def pop(self) -> int:
        if not self.head:
            return -1
        if not self.head.next:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        val = self.tail.val
        self.tail = self.tail.prev
        return val


    def popleft(self) -> int:
        if not self.head:
            return -1
        if not self.head.next:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        val = self.head.val
        self.head = self.head.next
        return val