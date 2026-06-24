class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = -float("inf")

        for i in nums:
            curSum = max(curSum, 0) + i
            maxSum = max(curSum, maxSum)

        return maxSum