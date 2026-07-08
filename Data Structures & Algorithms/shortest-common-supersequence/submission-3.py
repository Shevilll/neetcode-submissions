class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        cache = [[None] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        str1 = list(str1)
        str2 = list(str2)

        def dfs(i: int, j: int) -> list:
            if cache[i][j] is not None:
                return cache[i][j]
            if i == len(str1):
                cache[i][j] = str2[j:][::-1]
                return cache[i][j]
            if j == len(str2):
                cache[i][j] = str1[i:][::-1]
                return cache[i][j]

            if str1[i] == str2[j]:
                res = dfs(i + 1, j + 1) + [str1[i]]
            else:
                s1 = dfs(i + 1, j)
                s2 = dfs(i, j + 1)
                if len(s1) < len(s2):
                    res = s1 + [str1[i]]
                else:
                    res = s2 + [str2[j]]

            cache[i][j] = res
            return res

        return ''.join(reversed(dfs(0, 0)))