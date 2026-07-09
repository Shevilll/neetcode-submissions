class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        resIdx = 0
        for l in range(len(s)):
            i, j = l, l
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if maxLength < j - i + 1:
                    maxLength = j - i + 1
                    resIdx = i
                i -= 1
                j += 1
            
            i, j = l, l + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if maxLength < j - i + 1:
                    maxLength = j - i + 1
                    resIdx = i
                i -= 1
                j += 1
        
        return s[resIdx:resIdx+maxLength]