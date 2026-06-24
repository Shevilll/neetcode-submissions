class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        L = 0
        curr = 0

        for R in range(len(nums)):
            curr += nums[R]

            while curr >= target and L <= R:
                ans = min(ans, R - L + 1)
                curr -= nums[L]
                L += 1
        
        return 0 if ans == float('inf') else ans
        