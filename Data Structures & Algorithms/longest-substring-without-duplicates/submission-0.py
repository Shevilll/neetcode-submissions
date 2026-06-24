class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        ans = 0

        L = 0

        for R in range(len(s)):
            while s[R] in hashSet:
                hashSet.remove(s[L])
                L += 1
            hashSet.add(s[R])
            ans = max(ans, R - L + 1)

        return ans