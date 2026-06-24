class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        temp = 0
        ans = float("-inf")

        for R in range(len(s)):
            if L != R and s[L] != s[R]:
                if temp == k:
                    L = R
                    temp = 0
                else:
                    temp += 1
            ans = max(ans, R - L + 1)

        return 0 if ans == float('inf') else ans