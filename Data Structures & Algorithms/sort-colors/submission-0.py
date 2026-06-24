class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for i in nums:
            count[i] += 1

        i = 0
        for j in range(3):
            for k in range(count[j]):
                nums[i] = j
                i += 1
