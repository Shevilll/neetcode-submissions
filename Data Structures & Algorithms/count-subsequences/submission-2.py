class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        dp = [[-1] * M for i in range(N)]
        def dfs(i, j):
            if i == len(s) and j == len(t): return 1
            if i == len(s): return 0
            if j == len(t): return 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                dp[i][j] = dfs(i + 1, j) + dfs(i + 1, j + 1)
                return dp[i][j]
            
            dp[i][j] = dfs(i + 1, j)
            return dp[i][j]

        return dfs(0, 0)
