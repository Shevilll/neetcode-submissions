class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        stack = []
        for n in nums:
            stack.append(nums)
        if n in stack :
            return True 
        else:
            return false        