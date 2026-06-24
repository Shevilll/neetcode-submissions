class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)

        if len(stones) == 0:
            return 0

        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, -(y - x))
            if y < x:
                heapq.heappush(stones, -(x - y))
        return -stones[0] if stones else 0