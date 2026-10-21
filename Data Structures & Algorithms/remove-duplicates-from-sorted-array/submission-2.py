class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range (1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k        
       


































        # i = 0
        # j = 1

        # while j < len(nums):
        #     if nums[i] != nums[j]:
        #         i += 1
        #         nums[i] = nums[j]
        #     else:
        #         j += 1
        # return i + 1