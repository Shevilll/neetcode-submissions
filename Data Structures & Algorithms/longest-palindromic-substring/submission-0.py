class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j):
            maxLength = ""
            while i >= 0 and j < len(s) and s[i] == s[j]:
                maxLength = max(maxLength, s[i:j+1], key=len)
                i -= 1
                j += 1

            return maxLength

        length = ""
        for i in range(len(s)):
            length = max(length, helper(i, i), helper(i, i + 1), key=len)
        
        return length