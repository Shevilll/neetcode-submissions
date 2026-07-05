class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalSum = sum(stones)

        target = math.ceil(totalSum / 2)

        from functools import cache

        @cache
        def dfs(i, curr):
            if i >= len(stones) or curr >= target:
                return abs(curr - (totalSum - curr))

            res = min(dfs(i + 1, curr + stones[i]), dfs(i + 1, curr))

            return res

        return dfs(0, 0)
            