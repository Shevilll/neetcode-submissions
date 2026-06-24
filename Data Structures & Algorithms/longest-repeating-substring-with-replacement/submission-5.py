class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def isValid(x):
            dic = Counter(x)
            if len(dic) == 1: return True
            if k >= (len(x) - max(dic.values())): return True
            return False

        ans = float('-inf')
        L = 0

        for R in range(L, len(s)):
            if isValid(s[L:R+1]):
                ans = max(ans, R - L + 1)
            else:
                L += 1
        
        return 0 if ans == float('-inf') else ans