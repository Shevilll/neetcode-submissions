class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)

        dp = [0] * (M + 1)

        for i in range(N):
            curr = [0] * (M + 1)
            for j in range(M):
                if text1[i] == text2[j]:
                    curr[j + 1] = 1 + dp[j]
                else:
                    curr[j + 1] = max(curr[j], dp[j + 1])

            dp = curr

        return dp[M]