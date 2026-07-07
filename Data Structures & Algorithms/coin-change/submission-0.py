class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        M = amount

        dp = [float('inf')] * (M + 1)
        dp[0] = 0

        for i in range(N):
            currRow = [float('inf')] * (M + 1)
            currRow[0] = 0
            for c in range(1, M + 1):
                skip = dp[c]
                include = float('inf')

                if c - coins[i] >= 0:
                    include = 1 + currRow[c - coins[i]]
                currRow[c] = min(skip, include)

            dp = currRow

        return -1 if dp[amount] == float('inf') else dp[amount]