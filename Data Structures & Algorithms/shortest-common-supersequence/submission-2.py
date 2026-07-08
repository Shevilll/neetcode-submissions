class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        M, N = len(str1), len(str2)
        dp = [[None] * (N + 1) for i in range(M + 1)]

        s1, s2 = list(str1), list(str2)

        def dfs(i, j):
            if dp[i][j]: return dp[i][j]

            if i == M:
                dp[i][j] = s2[j:][::-1]
                return dp[i][j]
            if j == N:
                dp[i][j] = s1[i:][::-1]
                return dp[i][j]

            if s1[i] == s2[j]:
                res = dfs(i + 1, j + 1) + [s1[i]]
            else:
                opt1 = dfs(i + 1, j)
                opt2 = dfs(i, j + 1)

                if len(opt1) < len(opt2):
                    res = opt1 + [s1[i]]
                else:
                    res = opt2 + [s2[j]]

            dp[i][j] = res
            return res

        return "".join(reversed(dfs(0, 0)))