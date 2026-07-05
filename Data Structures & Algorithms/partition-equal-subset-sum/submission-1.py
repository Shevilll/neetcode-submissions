class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) // 2
        mem = [[-1] * int(target + 1) for i in range(len(nums))]

        def dfs(i, target):
            if target == 0: return True

            if i == len(nums) or target < 0: return False

            if mem[i][target] != -1: return mem[i][target]

            mem[i][target] = dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
            return mem[i][target]

        return dfs(0, target)