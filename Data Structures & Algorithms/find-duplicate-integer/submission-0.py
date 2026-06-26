class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while fast < len(nums):
            fast += 2
            slow += 1

            if fast < len(nums) and nums[fast] == nums[slow]:
                return nums[fast]

        while slow < len(nums):
            if nums[slow] == nums[-1]:
                return nums[slow]

        return -1