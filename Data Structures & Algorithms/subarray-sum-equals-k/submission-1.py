class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n

        pre = 0
        suf = 0
        for i in range(n):
            pre += nums[i]
            prefix[i] = pre
            suf += nums[n - i - 1]
            suffix[n - i - 1] = suf

        ans = 0

        for i in range(n):
            if prefix[i] >= k or suffix[i] >= k:
                ans += 1
        return ans
