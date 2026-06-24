class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-i for i in nums]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        temp = []

        for i in range(self.k):
            temp.append(heapq.heappop(self.heap))
        
        x = -temp[-1]

        for i in temp:
            heapq.heappush(self.heap, i)
        
        return x
