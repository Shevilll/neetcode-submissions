class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif r == m - 1 and c == n - 1:
                    dp[c] = 1
                elif c < n - 1:
                    dp[c] = dp[c] + dp[c + 1]
            
        return dp[0]
