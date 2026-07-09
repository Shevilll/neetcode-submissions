from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(i, j):
            if i < 0 or j == len(s): return 0

            if s[i] == s[j]:
                length = 1 if i == j else 2
                return length + dfs(i - 1, j + 1)

            return max(dfs(i - 1, j), dfs(i, j + 1))

        ans = 0
        for i in range(len(s)):
            ans = max(ans, dfs(i, i), dfs(i, i + 1))

        return ans