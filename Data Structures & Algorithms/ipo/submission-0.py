class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                heapq.heappush(maxProfit, -heapq.heappop(minCapital)[1])
            if not maxProfit:
                break
            w += -heapq.heappop(maxProfit)

        return w