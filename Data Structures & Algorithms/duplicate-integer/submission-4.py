class Solution:
    def hasDuplicate(self, nums: List[int]) ->bool:
        stack = []
        count = 0
        for n in nums:
            if n in stack:
                return True
            stack.append(n)
        return False        
                 

            


































        # return len(set(nums)) != len(nums)
        # stack = []
        # for n in nums:
        #     stack.append(nums)
        # if n in stack :
        #     return True 
        # else:
        #     return false        