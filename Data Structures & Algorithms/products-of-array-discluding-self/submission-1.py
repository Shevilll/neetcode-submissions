class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        pre = 1
        for i in range(1, n):
            pre *= nums[i - 1]
            prefix[i] = pre
        
        suf = 1
        for i in range(n - 2, -1, -1):
            suf *= nums[i + 1]
            suffix[i] = suf

        for i in range(n):
            nums[i] = prefix[i] * suffix[i]
        
        return nums