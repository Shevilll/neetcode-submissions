class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(i, nums, target, curr, res):
            if sum(curr) == target:
                res.append(curr.copy())
                return

            if i == len(nums):
                return

            curr.append(nums[i])

            if sum(curr) > target:
                helper(i + 1, nums, target, curr, res)
            else:
                helper(i, nums, target, curr, res)
            
            curr.pop()

            helper(i + 1, nums, target, curr, res)

        
        res = []

        helper(0, nums, target, [], res)

        return res