class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0

        def dfs(i, curr):
            if i == len(nums) and curr == target:
                ans += 1

            if i >= len(nums):
                return
                
            dfs(i + 1, curr + nums[i])
            dfs(i + 1, curr - nums[i])

        dfs(0, 0)
        return ans