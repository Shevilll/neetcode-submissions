class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.use = [0] * 1000
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.use[key] += 1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            x = float("inf")
            for i in self.cache.keys():
                if self.use[i] < x:
                    x = self.use[i]
            del self.cache[x]
            self.use[x] = 0
            self.size -= 1
            
        self.cache[key] = value
        self.use[key] += 1
        self.size += 1

