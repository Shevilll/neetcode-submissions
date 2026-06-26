class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while fast < len(nums):
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        while fast < len(nums):
            slow = nums[slow]
            fast = nums[fast]

            if fast == slow:
                return nums[fast]

        return -1