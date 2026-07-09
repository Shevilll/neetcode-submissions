class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[-1] * len(s) for i in range(len(s))]

        def dfs(i, j):
            if i < 0 or j == len(s): return 0

            if dp[i][j] != -1: return dp[i][j]

            if s[i] == s[j]:
                length = 1 if i == j else 2
                dp[i][j] = length + dfs(i - 1, j + 1)
                return dp[i][j]

            dp[i][j] = max(dfs(i - 1, j), dfs(i, j + 1))
            return dp[i][j]

        for i in range(len(s)):
            dfs(i, i)
            dfs(i, i + 1)

        ans = 0
        for i in dp:
            ans = max(ans, max(i))

        return ans