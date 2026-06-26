class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        if fast + 2 < len(nums) and nums[fast + 2] == nums[slow]:
            return nums[slow]

        while fast < len(nums):
            fast += 2
            slow += 1

            if fast < len(nums) and nums[fast] == nums[slow]:
                return nums[fast]

        while slow < len(nums):
            if nums[slow] == nums[-1]:
                return nums[slow]
            slow += 1

        return -1