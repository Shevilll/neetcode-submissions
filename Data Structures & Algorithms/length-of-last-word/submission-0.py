class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        i = 0

        while i < len(s):
            while not s[i].isalpha():
                i += 1
                if i == len(s):
                    return ans
            ans = 0
            while i < len(s) and s[i].isalpha():
                i += 1
                ans += 1
            
        return ans
        
