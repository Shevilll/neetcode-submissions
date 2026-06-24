class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        minSum = nums[0]
        currSum = 0
        currMin = 0

        for i in nums:
            currSum = max(currSum, 0) + i
            currMin = min(currMin, 0) + i
            maxSum = max(currSum, maxSum)
            minSum = min(currMin, minSum)

        total_sum = sum(nums)
        minKadane = total_sum - minSum
        if minKadane:
            return max(maxSum, minKadane)
        else:
            return maxSum