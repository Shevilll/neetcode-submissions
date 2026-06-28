class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i, res, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])

            helper(i + 1, res, curr)

            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            helper(i + 1, res, curr)

        
        res = []
        curr = []
        nums.sort()

        helper(0, res, curr)

        return res