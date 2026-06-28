class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, res, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])

            helper(i + 1, res, curr)

            curr.pop()

            helper(i + 1, res, curr)

        
        res = []
        curr = []

        helper(0, res, curr)

        return res