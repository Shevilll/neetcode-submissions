class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 2
        self.map = [None, None]

    def insert(self, key: int, value: int) -> None:
        i = key % self.capacity

        while True:
            if self.map[i] == None:
                self.map[i] = Pair(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.resize()
                return
            elif self.map[i].key == key:
                self.map[i].val = value
                return
            i += 1
            i = i % self.capacity

    def get(self, key: int) -> int:
        i = key % self.capacity
        while self.map[i] != None:
            if self.map[i].key == key:
                return self.map[i].val
            i += 1
            i = i % self.capacity
        return -1 

    def remove(self, key: int) -> bool:
        i = key % self.capacity

        while True:
            if self.map[i] == None:
                return False
            if self.map[i].key == key:
                self.map[i] = None
                self.size -= 1
                return True
            i += 1
            i = i % self.capacity

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = 2 * self.capacity

        newMap = [None] * self.capacity

        self.size = 0
        oldMap = self.map
        self.map = newMap

        for i in oldMap:
            if i:
                self.insert(i.key, i.val)
        
