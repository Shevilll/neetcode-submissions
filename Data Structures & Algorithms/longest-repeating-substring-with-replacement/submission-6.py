class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        ans = 0
        L = 0

        for R in range(len(s)):
            i = ord(s[R]) - 65
            count[i] += 1

            if (R - L + 1) - max(count) > k:
                count[ord(s[L]) - 65] -= 1
                L += 1
            else:
                ans = max(ans, R - L + 1)
        return ans

