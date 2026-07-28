class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0

        n = len(word1)
        m = len(word2)

        ans = ""

        while i < n and j < m:
            ans += word1[i]
            ans += word2[j]
            i += 1
            j += 1

        if i < n:
            ans += word1[i:]

        if j < m:
            ans += word2[j:]

        return ans