class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def dfs(i, j):
            if i == len(s) and j == len(t): return 1
            if i == len(s): return 0
            if j == len(t): return 1

            if s[i] == t[j]:
                return dfs(i + 1, j) + dfs(i + 1, j + 1)
            
            return dfs(i + 1, j)

        return dfs(0, 0)
