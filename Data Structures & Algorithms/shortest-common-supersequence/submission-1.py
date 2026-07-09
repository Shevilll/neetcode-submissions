from functools import cache

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def dfs(i, j):
            if i == len(str1): return str2[j:]
            if j == len(str2): return str1[i:]

            if str1[i] == str2[j]:
                return str1[i] + dfs(i + 1, j + 1)
            return min(str1[i] + dfs(i + 1, j), str2[j] + dfs(i, j + 1), key=len)

        return dfs(0, 0)