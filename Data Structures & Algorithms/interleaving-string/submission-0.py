from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(w1, w2, i, j):
            if i == len(w1) and j == len(w2): return 1
            if j == len(w2): return 1
            if i == len(w1): return 0

            if w1[i] == w2[j]:
                return dfs(w1, w2, i + 1, j + 1)

            return dfs(w1, w2, i + 1, j)

        return bool(dfs(s3, s1, 0, 0) and dfs(s3, s2, 0, 0))