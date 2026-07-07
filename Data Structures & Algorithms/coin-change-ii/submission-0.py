class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ans = 0

        def dfs(i, count):
            nonlocal ans
            if i == len(coins) or count > amount:
                return
            
            if count == amount:
                ans += 1
                return

            dfs(i, count + coins[i])
            dfs(i + 1, count)


        dfs(0, 0)
        return ans
