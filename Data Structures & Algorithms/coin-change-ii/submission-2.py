from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, count):
            if i == len(coins) or count > amount:
                return 0

            if count == amount:
                return 1
            
            return dfs(i, count + coins[i]) + dfs(i + 1, count)


        return dfs(0, 0)
