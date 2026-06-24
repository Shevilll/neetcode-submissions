class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.capacity = 1000
        self.map = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        i = key % 1000
        if self.map[i] == None:
            self.map[i] = ListNode(key, value)
            return
        
        curr = self.map[i]
        while curr.next:
            if curr.key == key:
                curr.val = value
                return
            curr = curr.next
        
        if curr.key == key:
            curr.val = value
            return
        curr.next = ListNode(key, value)


    def get(self, key: int) -> int:
        i = key % 1000
        if self.map[i]:
            curr = self.map[i]
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        i = key % self.capacity

        if self.map[i] == None:
            return
        curr = self.map[i]

        if curr.key == key:
            self.map[i] = self.map[i].next
            return
        
        while curr.next and curr.next.key != key:
            curr = curr.next
        
        curr.next = curr.next.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)