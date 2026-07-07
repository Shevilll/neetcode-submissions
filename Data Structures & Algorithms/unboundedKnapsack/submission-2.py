class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N = len(profit)
        M = capacity

        dp = [0] * (M + 1)

        for i in range(N):
            currRow = [0] * (M + 1)
            for c in range(1, M + 1):
                skip = dp[c]
                include = 0

                if c - weight[i] >= 0:
                    include = profit[i] + currRow[c - weight[i]]
                currRow[c] = max(include, skip)
            dp = currRow

        return dp[M]