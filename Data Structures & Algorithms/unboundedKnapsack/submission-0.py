class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        def dfs(i, c):
            if i == len(profit): return 0

            maxProfit = dfs(i+1, c)

            newCapacity = c - weight[i]
            if newCapacity >= 0:
                p = profit[i] + dfs(i, newCapacity)
                maxProfit = max(maxProfit, p)

            return maxProfit

        return dfs(0, capacity)
            