class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, second - first)

        stones.append(0)
        return abs(stones[0])        








































        # stones = [-i for i in stones]
        # heapq.heapify(stones)

        # if len(stones) == 0:
        #     return 0

        # while len(stones) > 1:
        #     x, y = -heapq.heappop(stones), -heapq.heappop(stones)
        #     if y != x:
        #         heapq.heappush(stones, -abs(y - x))
        # return -stones[0] if stones else 0